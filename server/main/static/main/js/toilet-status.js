function createTimeCounter(date, toilet_id, in_use){
    if (date){
        // Initially countdown is set to avoid the interval delay
        $("#toilet-counter-" + toilet_id).text(countdown(date).toString());
        return setInterval(function () {
            count = countdown(date);
            $("#toilet-counter-" + toilet_id).text(count.toString());
            total_time = 0;
            $("#toilet-" + toilet_id).attr("class", !in_use);

            if (in_use) {
              total_time = count.minutes*60 + count.seconds;
              $("#toilet-" + toilet_id).attr("class", !in_use);
              if (total_time > 60*2) {
                 $("#toilet-" + toilet_id).attr("class", "poo");
              }
              if (total_time > 60*10) {
                 $("#toilet-" + toilet_id).attr("class", "dead");
              }
            }
        }, 1000);
    }
}

$(function () {
    var time_counters = [];

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_host = $("[data-ws-host]").data("ws-host") != "" ? $("[data-ws-host]").data("ws-host") : window.location.host;
    var ws_path = ws_scheme + '://' + ws_host + "/stream/";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);

    // Set favicon animation
    var favicon = new Favico({bgColor : '#000000', textColor : '#FFFFFF', animation: 'slide'});
    var favicon_free = document.getElementById("favicon-free");
    var favicon_using = document.getElementById("favicon-using");

    socket.onmessage = function(message) {
        console.log("Got message " + message.data);
        var data = JSON.parse(message.data);
        var badge = $("[data-toilets-count]").data("toilets-count");

        // Set a time counter for each toilet
        $.each(data, function(index, item){
            $("#toilet-counter-" + item.toilet_id).attr("class", !item.in_use);
            clearTimeout(time_counters[item.toilet_id]);

            // If the toilet is free, show the last usage time
            if (!item.in_use){
                time_counters[item.toilet_id] = createTimeCounter(new Date(item.end_at), item.toilet_id, item.in_use);
                badge = (badge-1 < 0) ? 0 : (badge - 1);
                $.get('toilet/' + item.toilet_id +'/last_usage_time', function(data){
                    $("#toilet-last-usage-" + item.toilet_id).show();
                    total_time = moment.duration(data.usage_time, "seconds").humanize();
                    $("#toilet-last-usage-time-" + item.toilet_id).text(total_time);
                });
            }else{
                time_counters[item.toilet_id] = createTimeCounter(new Date(item.start_at), item.toilet_id, item.in_use);
                $("#toilet-last-usage-" + item.toilet_id).hide();
            }
        });
        if (badge == 0){
            favicon.image(favicon_free);
        }else{
            favicon.image(favicon_using);
            favicon.badge(badge);
            // If favicon image was changed badge has to be set twice
            // in order to view the correct number in the favicon badge.
            favicon.badge(badge);
        }
    };
    // Helpful debugging
    socket.onopen = function() {
        console.log("Connected to notification socket");
        $.get('toilets/last_event')
    };
    socket.onclose = function() {
        console.log("Disconnected to notification socket");
    };
});
