$(document).ready(() => {
  const showPage = () => {
    $('#loader-container').css('display', 'none');
    $('#root').css('display', 'block');
  };

  const hidePage = () => {
    $('#loader-container').css('display', 'flex');
    $('#root').css('display', 'none');
  };

  hidePage();

  const username = $('#profile-username');
  const intro = $('#profile-intro');
  const fullname = $('#profile-fullname');
  const email = $('#profile-email');
  const bio = $('#profile-bio');
  const address = $('#profile-address');
  const image = $('#profile-image');

  $.ajax({
    url: '/user/profile/json',
    success: function (result) {
      const res = result[0].fields;

      username.text(res.username);
      intro.text(res.short_intro);
      fullname.text(res.name);
      email.text(res.email);
      bio.text(res.bio);
      address.text(res.address);
      // profiles/default-user_pfzkxt
      if (res.profile_image === 'profiles/default-user_pfzkxt') {
        image.attr(
          'src',
          `https://res.cloudinary.com/da66vxlpb/image/upload/v1/images/media/${res.profile_image}`
        );
      } else {
        image.attr(
          'src',
          `https://res.cloudinary.com/da66vxlpb/image/upload/v1/${res.profile_image}`
        );
      }
      image.attr('alt', res.name);

      showPage();
    },
  });
});
