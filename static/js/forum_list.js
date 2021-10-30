$(function (){

    var $stack = $('#list');

    $.ajax({
        type: 'GET',
        url: 'json',
        success: function(data) {
            console.log(data);
            $.each(data, function(ind, dict) {
                console.log(dict);
                var forum = dict['fields'];
                console.log(dict['fields']);
                if (forum['creator_image'] == 'profiles/default-user_pfzkxt'){
                    forum['creator_image'] = 'https://res.cloudinary.com/da66vxlpb/image/upload/v1/images/media/' + forum['creator_image'];
                }else{
                    forum['creator_image'] = 'https://res.cloudinary.com/da66vxlpb/image/upload/v1/' + forum['creator_image'];
                }
                $stack.append('<div class="card" id = "' + dict['pk'] + '" onClick="reply_click(this.id)"><div class="card-body"><p class="h4">' + forum['title'] + '</p><div class="user"><div class="d-flex flex-column"><div class="container"><div class = "image_user"><img src="' + forum['creator_image'] + '" class="float-start" style = "margin-right: 10px; object-fit: fill;  border-radius: 50%;" width="30" height="30" alt=""></div><p class="h6 text-muted" style="padding-top: 3px">' + forum['creator_username'] + ' - ' + forum['created_at'] + '</p></div><div class="container"><p class="deskripsi">' + forum['message'] + '</p></div></div></div></div></div>');
            });
        }
    });

    
});

function reply_click(clicked_id){
    window.location = window.location + clicked_id;
}

function create_forum(){
    window.location = window.location + 'add/';
}

//'<div class="card" id = "' + dict['pk'] + '"><div class="card-body"><p class="h4">' + forum['title'] + '</p><div class="user"><div class="d-flex flex-column"><div class="container"><div class = "image_user"><img src="' + forum['creator_image'] + '" class="rounded float-start" alt=""></div><p class="h6 text-muted">' + forum['creator_username'] + ' - ' + forum['created_at'] + '</p></div><div class="container"><p class="deskripsi">' + forum['title'] + '</p></div></div></div></div></div>'