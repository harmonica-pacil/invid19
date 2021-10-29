$(function () {

    var view = $('#comment_list');
    view.empty();

    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/comment/json/',
        success: function (data) {
            console.log(data);
            $.each(data, function (ind, dict) {
                console.log(dict);
                var comment = dict['fields'];
                console.log(dict['fields']);
                if (comment['creator_image'] == 'profiles/default-user_pfzkxt') {
                    comment['creator_image'] = 'https://res.cloudinary.com/da66vxlpb/image/upload/v1/images/media/' + comment['creator_image'];
                } else {
                    comment['creator_image'] = 'https://res.cloudinary.com/da66vxlpb/image/upload/v1/' + comment['creator_image'];
                }
                var $a = comment['created_at']
                
                view.append('<div class="card"><div class="card-body"><p class="h4">' + comment['message'] + '</p><div class="user"><div class = "image_user"><img src="' + comment['creator_image'] + '" class="rounded float-start" alt=""></div><p class="h6 text-muted">' + comment['commet_creator_username']  + '-' + $a + '</p></div></div></div>');
            });
        }
    });
});

// $(document).ready(function() {
//     $('#submit').click(function(e) {  
//       alert(1);
//     });
// });