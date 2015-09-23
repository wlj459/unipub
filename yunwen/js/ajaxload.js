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
				"page_num": AjaxLoad.page,
			},
			success: function(html) {
				var lastPage = html.match(/<input type="hidden" name="lastpage" value="(True|False)">/)[1] == 'True' ? true : false;
				$(AjaxLoad.parameter.targetSelector).append(html);
				if (lastPage) {
					$(AjaxLoad.parameter.ajaxLoadText).remove();
					AjaxLoad.status = 1;
				}
				AjaxLoad.page += 1;
			},
			complete: function() {
				status = 0;
			}
		});
	},
	scrollEvent: function () {
		var scrollTop = $(this).scrollTop();
		var windowHeight = this.innerHeight;
		var scrollHeight = $(document).height();

		if(scrollTop + windowHeight >= scrollHeight) {
			AjaxLoad.loadData();
		}
	},
	page: 1,
	status: 0,
}