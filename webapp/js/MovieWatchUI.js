var MovieWatchIntegration = new MovieWatchIntegration();
var MovieWatchUI = (function () {
    function MovieWatchUI() {
    }

    MovieWatchUI.prototype.login = function () {
        var id = $('#address').val();
        var password = $('#password').val();
        MovieWatchIntegration.login(id, password)
    };

    return MovieWatchUI;
})();

