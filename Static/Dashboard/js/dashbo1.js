var ctx = document.getElementById("myChart").getContext("2d");
var valuec;
if (data.condition == 'true') {
  console.log(data.condition)
    valuec = data.z;
    console.log(valuec)
  }
  else{
    valuec = data.y;
  }


var myChart = new Chart(ctx, {
  type: data.type,
  data: {
    labels: data.x,
    datasets: valuec,
    // datasets: [
    //   {
    //     label: data.label,
    //     data: data.y,
    //     fill: false,
    //     backgroundColor: "rgba(255, 99, 132, 0.2)",
    //     borderColor: "rgba(255, 99, 132, 1)",
    //     borderWidth: 1,
    //   }
    // ],
  },
  options: {
    title: {
      display: true,
      text: data.title,
    },
    legend: {
      display: true,
      position: "top",
      labels: {
        // fontColor: 'rgb(255, 99, 132)'
      },
    },
    scales: {
      yAxes: [
        {
          ticks: {
            // Include a dollar sign in the ticks
            callback: function (value, index, values) {
              return "$" + value;
            },
          },
        },
      ],
    },
  },
});
