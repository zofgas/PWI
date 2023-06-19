let toggle = button => {
    let element = document.getElementById("myfooter");
    let hidden = element.getAttribute("hidden");

    if (hidden) {
       element.removeAttribute("hidden");
       button.innerText = "Hide footer";
    } else {
       element.setAttribute("hidden", "hidden");
       button.innerText = "Show footer";
    }
  }
   



  document.addEventListener('DOMContentLoaded', () => {
    const profileListLink = document.getElementById('profile-list-en-link');
    const container = document.querySelector('.container');
          
    profileListLink.addEventListener('click', (event) => {
      event.preventDefault();
      
      fetch('/profile_list_en/')
        .then(response => response.text())
        .then(data => {
          container.innerHTML = data;
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    const profileListLink = document.getElementById('gallery-en-link');
    const container = document.querySelector('.container');
          
    profileListLink.addEventListener('click', (event) => {
      event.preventDefault();
      
      fetch('/gallery_en/')
        .then(response => response.text())
        .then(data => {
          container.innerHTML = data;
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });
  });