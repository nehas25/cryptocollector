// Reference: https://openfolder.sh/django-tutorial-as-you-type-search-with-ajax

const user_input = $('#user-input')
const search_icon = $('#search-icon')
const coins_div = $('#replaceable-content')
const endpoint = '/coins/'
const delay_by_in_ms = 700
let scheduled_function = false

let ajax_call = function(endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            //fade out the coins_div, then
            coins_div.fadeTo('slow', 0).promise().then(() => {
                //replace the HTML contents
                coins_div.html(response['html_from_view'])
                //fade-in the div with new contents
                coins_div.fadeTo('slow', 1)
                //stop animating the search icon
                search_icon.removeClass('blink')
            })
        })
}

user_input.on('keyup', function() {
    const request_parameters = {
        q: $(this).val()
    }

    //start animating the search icon
    search_icon.addClass('blink')

    // if scheduled_function is NOT false, cancel the execution of the function
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    // setTimeout returns the ID of the function to be executed
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})