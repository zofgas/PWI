document.addEventListener('DOMContentLoaded', () => {
    const profileListLink = document.getElementById('profile-list-link');
    const container = document.querySelector('.container');
          
    profileListLink.addEventListener('click', (event) => {
      event.preventDefault();
      
      fetch('/profile_list/')
        .then(response => response.text())
        .then(data => {
          container.innerHTML = data;
        })
        .catch(error => {
          console.error('Wystąpił błąd:', error);
        });
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    const profileListLink = document.getElementById('gallery-link');
    const container = document.querySelector('.container');
          
    profileListLink.addEventListener('click', (event) => {
      event.preventDefault();
      
      fetch('/gallery/')
        .then(response => response.text())
        .then(data => {
          container.innerHTML = data;
        })
        .catch(error => {
          console.error('Wystąpił błąd:', error);
        });
    });
  });

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
   
