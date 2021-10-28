$(function (){

    var $stack = $('#list');
    $stack.empty();

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
                $stack.append('<div class="card"><div class="card-body"><p class="h4">' + forum['title'] + '</p><div class="user"><div class = "image_user"><img src="' + forum['creator_image'] + '" class="rounded float-start" alt=""></div><p class="h6 text-muted">' + forum['creator_username'] + ' - ' + forum['created_at'] + '</p></div></div></div>');
            });
        }
    });
});