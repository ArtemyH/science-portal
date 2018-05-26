require(['jquery', 'js-cookie'], function ($, cookie) {
    $(document).ready(function () {
        $('.delete-attachment').on('click', function() {
            var $this = $(this);
            $.ajax({
                url: $this.data('deleteUrl'),
                type: 'DELETE',
                beforeSend: function(xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", cookie.get('csrftoken'));
                },
                success: function(result) {
                    $this.parents('tr').remove();
                }
            }).fail(function(data) {

            });
        });
    });
});
