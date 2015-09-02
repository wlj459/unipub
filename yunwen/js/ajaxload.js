var AjaxLoad = {
	parameter: {
		targetSelector: "",
		ajaxLoadText: ".ajaxloading",
		ajax: {
			method: "get",
			url: "",
		}
	},
	init: function (parameter) {
		$.extend(AjaxLoad.parameter, parameter);

		$(window).scroll(AjaxLoad.scrollEvent);

		AjaxLoad.loadData();
	},
	loadData: function () {
		if(AjaxLoad.status != 0) {
			return false;
		}
		status = 1;
		$.ajax({
			method: AjaxLoad.parameter.ajax.method,
			url: AjaxLoad.parameter.ajax.url,
			data: {
				"page": AjaxLoad.page,
			},
			success: function(data) {
				AjaxLoad.page += 1;
				$(AjaxLoad.parameter.targetSelector).append(data.content);
				if (data.lastPage) {
					$(AjaxLoad.parameter.ajaxLoadText).remove();
				}
			},
			complete: function() {
				status = 0;
			}
		});
	},
	scrollEvent: function () {
		var scrollTop = $(this).scrollTop();
		var windowHeight = $(this).height();
		var scrollHeight = $(document).height();

		console.log(scrollTop, windowHeight, scrollHeight)
		if(scrollTop + windowHeight >= scrollHeight) {
			AjaxLoad.loadData();
		}
	},
	page: 1,
	status: 0,
}