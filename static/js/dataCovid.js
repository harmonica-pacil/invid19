$(document).ready(() => {
  $.ajax({
    url: 'https://apicovid19indonesia-v2.vercel.app/api/indonesia',
    success: function (result) {
      document.getElementById('kasus-positif').textContent =
        result['positif'].toLocaleString();
      document.getElementById('kasus-sembuh').textContent =
        result['sembuh'].toLocaleString();
      document.getElementById('kasus-meninggal').textContent =
        result['meninggal'].toLocaleString();
    },
  });

    $("#search").keypress(function(e) {
        if(e.which == 13) {
            var q = e.currentTarget.value.toUpperCase();
            console.log(q)
            $.ajax({
                url: "https://indonesia-covid-19.mathdro.id/api/provinsi/" ,
                async: true,
      

                success: function(result_) {

                  var result;

                  $.each(result_.data, function (ind,dict) {
                    if( dict.provinsi.toLowerCase() === q.toLowerCase()) result = dict;              
                  });
                  console.log(result)
                  console.log(result_)

                    var view = $('#target-ajax');
                    view.empty();
                    view.append(
                        `<h4> Kasus Covid-19 di Provinsi ${result["provinsi"]} </h2>
                        <div class = "container-Indonesia-text">
                        </div>
                        <div class = "container-Indonesia-card">
                            <div class="card text-white bg-danger mb-3" style="max-width: 18rem;border-radius: 8px;">
                                <div class="card-header">Positif</div>
                                <div class="card-body">
                                <p class="card-text">${result["kasusPosi"].toLocaleString()}</p>
                                </div>
                            </div>
                            <div class="card text-white bg-success mb-3" style="max-width: 18rem;border-radius: 8px;">
                                <div class="card-header">Sembuh</div>
                                <div class="card-body">
                                <p class="card-text">${result["kasusSemb"].toLocaleString()}</p>
                                </div>
                            </div>
                            <div class="card text-white bg-secondary mb-3" style="max-width: 18rem;border-radius: 8px;">
                                <div class="card-header">Meninggal</div>
                                <div class="card-body">
                                <p class="card-text">${result["kasusMeni"].toLocaleString()}</p>
                                </div>
                            </div>
                        </div>` 
                    )
                },
            })
        }

    })
})
