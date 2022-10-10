var vg_1 = "visualise_shot_chart.json";
vegaEmbed("#shot_chart", vg_1).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var vg_2 = "visualise_squiggle.json";
vegaEmbed("#squiggle", vg_2).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
    }).catch(console.error);