var MovieWatchIntegration = new MovieWatchIntegration();
var MovieWatchUI = (function () {
    function MovieWatchUI() {
    }

    MovieWatchUI.prototype.login = function () {
        var id = $('#address').val();
        var password = $('#passord').val();
        MovieWatchIntegration.login(id, password)
    };

    return MovieWatchUI;
})();

