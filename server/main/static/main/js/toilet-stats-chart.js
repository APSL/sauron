function newChart(container_id, categories, visit_values, time_values) {
  Highcharts.chart(container_id, {
    chart: {
        type: 'column',
        width: 1100
      },
      title: {
        text: ''
      },
      xAxis: {
        "categories": categories,
        "title": {"text": "Hour"}
      },
      yAxis: [{
        title: {
            text: 'Visits'
        }
      }, {
        title: {
          text: 'Time (hours)'
        },
        opposite: true
      }],
      legend: {
        shadow: false
      },
      tooltip: {
        shared: true
      },
      plotOptions: {
        column: {
          grouping: false,
          shadow: false,
          borderWidth: 0
        }
      },
      series: [{
        name: 'Visits',
        data: visit_values,
        pointPadding: 0.3,
        pointPlacement: -0.2
      }, {
        name: 'Time',
        data: time_values,
        pointPadding: 0.4,
        pointPlacement: -0.2,
        yAxis: 1
      }]
    }
  );
}
