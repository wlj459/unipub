var UserPhoto = {
	index: 0,
	length: 0,
	parameter: {
		dataSelector: '.form-userphoto-data',
		imageSelector: '.form-userphoto-img',
		buttonSelector: '.form-userphoto-btn',
		inputSelector: '#form-userphoto',
	},
	data: [],
	init: function (parameter) {
		$.extend(UserPhoto.parameter, parameter);

		UserPhoto.length = $(UserPhoto.parameter.dataSelector + ' > li').length;
		UserPhoto.index = UserPhoto.length  - 1;

		for (var i = 0; i < UserPhoto.length; i ++) {
			UserPhoto.data.push({
				url: $($(UserPhoto.parameter.dataSelector + ' > li')[i]).attr('data-url'),
				val: $($(UserPhoto.parameter.dataSelector + ' > li')[i]).attr('data-value')
			});
		}

		UserPhoto.changeImage();

		$(UserPhoto.parameter.buttonSelector).click(function () {
			UserPhoto.changeImage();

			return false;
		});
	},
	changeImage: function () {
		UserPhoto.index ++;
		if (UserPhoto.index === UserPhoto.length) {
			UserPhoto.index = 0;
		}
		$(UserPhoto.parameter.imageSelector).attr('src', UserPhoto.data[UserPhoto.index].url);
		$(UserPhoto.parameter.inputSelector).val(UserPhoto.data[UserPhoto.index].val);
	},
}
