tinyMCE.init({
                                 
    mode : "textareas",
                                 
    theme : "modern",
                                 
    width: '780px',
                                 
    language: 'zh_CN',
                                 
    plugins: [
                                 
        "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak spellchecker",
                                 
        "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
                                 
        "table contextmenu directionality emoticons template textcolor paste fullpage textcolor"
                                 
    ],
                                 
    menubar: false,
                                 
    toolbar_items_size: 'small',
                                 
    toolbar1: "undo redo | bold italic underline strikethrough forecolor backcolor | alignleft aligncenter alignright | bullist blockquote link unlink code | pagebreak preview fullscreen | fontselect fontsizeselect",
                                 
    content_css : '/static/js/tinymce/skins/custom/custom.css'
                                 
});
