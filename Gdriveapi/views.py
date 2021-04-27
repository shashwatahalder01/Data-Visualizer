from django.shortcuts import render, HttpResponse
from . models import Product

# for accessing gdrive
import os
import os.path
from pathlib import Path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
# for download file from gdrive
import io
from googleapiclient.http import MediaIoBaseDownload
# for db
from django.db import transaction

# for read excelfile

import pandas as pd
import numpy as np

# for draw chart
import matplotlib.pyplot as plt
import matplotlib.dates as dates

def home(requests):

    service= connectDrive()
    fileDownload(service)
    #insertintoDb()
    #plotGrapf()
    return render(requests,'Gdriveapi/index.html')




def connectDrive():

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    
    creds = None
    token_path=os.path.join(os.path.dirname(__file__),'drivecredentials','token.json')  
    credentials_path=os.path.join(os.path.dirname(__file__),'drivecredentials','credentials.json')
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
 
    return service




def fileDownload(service):

    # Search File
    
    results = service.files().list(q="name = 'Price List.xlsx'").execute()
    items = results.get('files', [])

    # File Download
    
    if items:
        for item in items:
            file_id = item['id']
            file_name = item['name']

            request = service.files().get_media(fileId=file_id)
            fh = io.BytesIO()

            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                done = downloader.next_chunk()

            fh.seek(0)
            dirname = Path(__file__).resolve().parent.parent
            file_location = os.path.join(dirname,'Static','Gdriveapi', file_name)
            with open(file_location, 'wb') as f:
                f.write(fh.read())
                f.close()



@transaction.atomic
def insertintoDb():

    # read xlsx from directory
    # Product.objects.all().delete()

    dirname = Path(__file__).resolve().parent.parent
    file_name = 'Price List.xlsx'
    file_location = os.path.join(dirname,'Static','Gdriveapi', file_name)
    df = pd.read_excel(file_location, header=3, usecols='B:I')

    # write in db

    for i in df.itertuples():
        dbdata = Product(date=i[1], chal=i[2], dal=i[3], salt=i[4],
                          oil=i[5], honey=i[6], butter=i[7], milk=i[8])
        dbdata.save()




def plotGrapf():

    
    l = []
    m = []
    a = Product.objects.values_list('date')
    b = Product.objects.values_list('chal')
    for item in a:
        l = l+list(item)
    for item in b:
        m = m+list(item)

    plt.plot(l[1:32], m[1:32], 'ro-', linewidth=.5, label='Chal  Price')
    plt.legend()
    plt.title('Price in January')
    plt.xlabel('January')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.show()

    


    """
    # Image save

    dirname = os.path.dirname(__file__)
    imgfile_name = 'img.png'
    imgfile_location = os.path.join(dirname,'static','api', imgfile_name)
    plt.savefig(imgfile_location)

    #a={ 'img':'D:\\Django\\DriveApiProject\\Driveapi\\api\\img.png'}
    

    # plot graph

    ax = plt.gca()
    xaxis = dates.date2num(df.Date.head(30))    # Convert to maplotlib format
    hfmt = dates.DateFormatter('%d')
    ax.xaxis.set_major_formatter(hfmt)
    ax.xaxis.set_major_locator(dates.DayLocator())

    ymax = max(df.Chal.head(30))
    ymin = min(df.Chal.head(30))
    # ax.set_xlim()
    # ax.set_ylim(ymin,ymax)
    plt.ylim(ymin, ymax)
    plt.plot(xaxis, df.Chal.head(30), 'ro-', linewidth=.5, label='Chal  Price')
    plt.legend()
    plt.title('Price in January')
    plt.xlabel('January')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.show()
    #imgfile_name = 'img.png'
    #imgfile_location = os.path.join(dirname, imgfile_name)
    # plt.savefig(imgfile_location)
    # a=imgfile_location
    #b= "< img src='"+ a+"' alt='Graph' >"

  
    
    """