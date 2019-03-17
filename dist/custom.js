function chart_interaction(chart,chartui)
        {
        this.chart=chart;
        this.chartui=chartui;
            
    
        $("#"+this.chartui+" .ui_home:first").click(
                function() {chart.zoomOut();});

        $("#"+this.chartui+" .btn-group-toggle:first .btn").on('click', function(event) {
                  nb_series=chart.series.length;
                  var val = $(this).find('input').val();
                  var enableMouseTracking;
                  var zoom;
                  if (val=="marker")
                        {
                        enableMouseTracking=true;
                        zoom=null;
                        }
                  if (val=="zoom")
                       {
                       enableMouseTracking=false;
                       zoom="xy";
                       }
                                                               
                                                               
                  for (var indice=0;indice<nb_series;indice++)
                    {
                    chart.series[indice].update({enableMouseTracking: enableMouseTracking});
                    }
                        
                chart.update({chart: {zoomType: zoom}});
                                                               
            });

        }



