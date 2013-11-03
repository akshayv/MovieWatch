/**
 * Created with PyCharm.
 * User: akshay
 * Date: 11/3/13
 * Time: 6:27 PM
 * To change this template use File | Settings | File Templates.
 */

var MovieWatchIntegration = (function () {
    function MovieWatchIntegration(){}
    var baseURL = String('http://localhost:5000');


    function makeJQueryJSONCall(servletURL, callbackFunction) {
        $.getJSON(servletURL, function (response) {
            callbackFunction(response);
        });
    }


    MovieWatchIntegration.prototype.login = function (userId, password) {
        var servletUrl = baseURL + '/login?';
        servletUrl += 'emailId=' + userId;
        servletUrl += '&password=' + password;
        makeJQueryJSONCall(servletUrl, function() {
            alert('Alright!');
        })
    };

    return MovieWatchIntegration;
})();

