$(document).ready(() => {
    $("#search").keypress(function(e) {
        if(e.which == 13) {
            var q = e.currentTarget.value.toUpperCase();
            console.log(q)
            $.ajax({
                url: "/covid19-provinsi" + q,
                async: true,
                success: function(result) {
                    var view = $('#target-ajax');
                    view.empty();
                    for(var i = 0; i < result.length; i++) {
                        if(view[i] != undefined) {
                            view.append(
                                // `<h2> Kasus Covid-19 di Provinsi ${result[i]["Provinsi"]} </h2>`
                                `<div class = "container-Indonesia-text">
                                <h1>Kasus Covid-19 di Provinsi ${result[i]["Provinsi"]} </h1>
                                </div>
                                <div class = "container-Indonesia-card">
                                    <div class="card text-white bg-danger mb-3" style="max-width: 18rem;">
                                        <div class="card-header">Positif</div>
                                        <div class="card-body">
                                        <p class="card-text">${result[i]["Kasus_Posi"]}</p>
                                        </div>
                                    </div>
                                    <div class="card text-white bg-success mb-3" style="max-width: 18rem;">
                                        <div class="card-header">Sembuh</div>
                                        <div class="card-body">
                                        <p class="card-text">${result[i]["Kasus_Semb"]}</p>
                                        </div>
                                    </div>
                                    <div class="card text-white bg-dark mb-3" style="max-width: 18rem;">
                                        <div class="card-header">Meninggal</div>
                                        <div class="card-body">
                                        <p class="card-text">${result[i]["Kasus_Meni"]}</p>
                                        </div>
                                    </div>
                                </div>`
                                // '<tr><th>Item</th><th>Detail</th></tr>' +
                                // '<tr><td>Provinsi </td>' + '<td>' + result[i]["Provinsi"] + '</td>' +
                                // '<tr><td>Kasus Positif </td>' + '<td>' + result[i]["Kasus_Posi"] + '</td>' +
                                // '<tr><td>Kasus Sembuh </td>' + '<td>' +result[i]["Kasus_Semb"] + '</td>'  +
                                // '<tr><td>Kasus Meninggal </td>' + '<td>' + result[i]["Kasus_Meni"] + '</td>' 
                            )
                        }
                    }
                },
            })
        }

    })
})