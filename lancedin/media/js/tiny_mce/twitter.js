// tweet_link
$('.tweet_link').click(function(e){
    link_id = $(this).attr('data-link_id');
    var target = $(this);
    tweetLink(target);
});

function tweetLink(t){
    link_id = t.attr('data-link_id');
    $.ajax({
        type: "POST",
        data: { "link_id": link_id, "csrfmiddlewaretoken": csrfmiddlewaretoken},
        url: "/tweet_link",
    });     
};  
