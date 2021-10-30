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

  $('#search').keypress(function (e) {
    if (e.which == 13) {
      var q = e.currentTarget.value.toUpperCase();
      console.log(q);
      $.ajax({
        url: 'covid19-provinsi?q=' + q,
        async: true,
        success: function (result) {
          var view = $('#target-ajax');
          view.empty();
          for (var i = 0; i < result.length; i++) {
            if (view[i] != undefined) {
              view.append(
                `<h4> Kasus Covid-19 di Provinsi ${result[i]['Provinsi']} </h2>
                                <div class = "container-Indonesia-text">
                                </div>
                                <div class = "container-Indonesia-card">
                                    <div class="card text-white bg-danger mb-3" style="max-width: 18rem;border-radius: 8px;">
                                        <div class="card-header">Positif</div>
                                        <div class="card-body">
                                        <p class="card-text">${result[i][
                                          'Kasus_Posi'
                                        ].toLocaleString()}</p>
                                        </div>
                                    </div>
                                    <div class="card text-white bg-success mb-3" style="max-width: 18rem;border-radius: 8px;">
                                        <div class="card-header">Sembuh</div>
                                        <div class="card-body">
                                        <p class="card-text">${result[i][
                                          'Kasus_Semb'
                                        ].toLocaleString()}</p>
                                        </div>
                                    </div>
                                    <div class="card text-white bg-secondary mb-3" style="max-width: 18rem;border-radius: 8px;">
                                        <div class="card-header">Meninggal</div>
                                        <div class="card-body">
                                        <p class="card-text">${result[i][
                                          'Kasus_Meni'
                                        ].toLocaleString()}</p>
                                        </div>
                                    </div>
                                </div>`
              );
            }
          }
        },
      });
    }
  });
});
