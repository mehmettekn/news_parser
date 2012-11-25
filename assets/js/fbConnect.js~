
// Additional JS functions here
var login_button;
var logout_button;
var userInfo;    
    
function showLogout(status){
    if (status)
        logout_button.style.display = 'block';
    else
        logout_button.style.display = 'none';
};

window.fbAsyncInit = function() {
    FB.init({
        appId      : '291562957621247', // App ID
        channelUrl : '//http://mehmetsapp.appspot.com/channel', // Channel File
        status     : true, // check login status
        cookie     : true, // enable cookies to allow the server to access the session
        xfbml      : true,  // parse XFBML
        oauth      : true         
    });

    // Additional init code here
    
    function updateButton(response) {
        login_button = document.getElementById("fb-auth");
        logout_button = document.getElementById("fb-logout");            
        userInfo = document.getElementById("user-info");
        if (response.authResponse)  {
            //user already logged in
            showLogout(true)                
            FB.api('/me', function(info) {
                login(response, info);
            });
            logout_button.onclick = function() {
                FB.logout(function(response) {
                    logout(response);
                });
            };
        } else {
           //user is not connected to your app or logged out
            showLogout(false)                
            login_button.onclick = function() {
                FB.login(function(response) {
                    if (response.authResponse) {
                        FB.api('/me', function(info) {
                            login(response, info);
                        });	   
                    } else {
                        //user cancelled login or did not grant authorization
                        userInfo.innerHTML = "<h2>Login olsana kardesim adami ayar etme artiz!</h2>"
                    }
                }, {scope:'email,user_birthday,status_update,publish_stream,user_about_me'});  	
            }
        }
    }
 
    // run once with current status and whenever status changes
    FB.getLoginStatus(updateButton);
    FB.Event.subscribe('auth.statusChange', updateButton);
};
  
(function() {
    var e = document.createElement('script'); e.async = true;
    e.src = document.location.protocol
        + '//connect.facebook.net/en_US/all.js';
    document.getElementById('fb-root').appendChild(e);
}());
  
function login(response, info) {
    if (response.authResponse) {
        var accessToken = response.authResponse.accessToken;
        userInfo.innerHTML = '<img src="https://graph.facebook.com/' + info.id + '/picture">' + info.name
        //button.innerHTML = 'Logout';
        showLogout(true)
    }
}
  
function logout(response) {
    userInfo.innerHTML = "";
    (function(d){
        var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
        if (d.getElementById(id)) {return;}
            js = d.createElement('script'); js.id = id; js.async = true;
            js.src = "//connect.facebook.net/en_US/all.js";
            ref.parentNode.insertBefore(js, ref);
    }(document));
}

