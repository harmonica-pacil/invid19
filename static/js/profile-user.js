const displayPage = () => {
  document.querySelector('#loader-container').style.display = 'none';
  document.querySelector('#root').style.display = 'block';
};

const hidePage = () => {
  document.querySelector('#loader-container').style.display = 'flex';
  document.querySelector('#root').style.display = 'none';
};

hidePage();

const username = document.getElementById('profile-username');
const intro = document.getElementById('profile-intro');
const fullname = document.getElementById('profile-fullname');
const email = document.getElementById('profile-email');
const bio = document.getElementById('profile-bio');
const address = document.getElementById('profile-address');
const image = document.getElementById('profile-image');

const xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    const res = JSON.parse(this.responseText)[0].fields;
    username.innerHTML = res.username;
    intro.innerHTML = res.short_intro;
    fullname.innerHTML = res.name;
    email.innerHTML = res.email;
    bio.innerHTML = res.bio;
    address.innerHTML = res.address;
    // profiles/default-user_pfzkxt
    if (res.profile_image === 'profiles/default-user_pfzkxt') {
      image.src = `https://res.cloudinary.com/da66vxlpb/image/upload/v1/images/media/${res.profile_image}`;
    } else {
      image.src = `https://res.cloudinary.com/da66vxlpb/image/upload/v1/${res.profile_image}`;
    }
    image.alt = res.name;
    setTimeout(displayPage, 2500);
  }
};
xhttp.open('GET', '/user/profile/json', true);
xhttp.send();
