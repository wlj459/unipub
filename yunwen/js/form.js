var MyForm = {
	parameter: {},
	checkMobilephone: function (str) {
		return MyForm.regExpCheck(/^1(3|4|5|8)[0-9]\d{8}$/, str)
	},
	checkEmail: function (str) {
		return MyForm.regExpCheck(/^[a-zA-Z0-9]\w+@(\w+.)+[a-z]{2,4}$/, str)
	},
	checkQQ: function (str) {
		return MyForm.regExpCheck(/^[1-9][0-9]{4,9}$/, str)
	},
	checkLength: function (str, maxLen) {
		if (str.length > maxLen) {
			return false;
		} else {
			return true;
		}
	},
	checkNull: function (str) {
		if (!str || /^\s+$/.test(str)) {
			return true;
		} else {
			return false;
		}
	},
	clearHint: function () {
		var hintTexts = document.querySelectorAll('.form-hint.error');
		for (var i = 0; i < hintTexts.length; i ++) {
			hintTexts[i].textContent = '';
		}
	},
	addHint: function (key, text) {
		var hintTextNode = document.querySelector(key).parentNode.parentNode.querySelector('.form-hint.error');
		if(hintTextNode) {
			hintTextNode.textContent = text;
		} else {
			document.querySelector(key).parentNode.outerHTML += '<p class="form-hint error">' + text + '</p>';
		}
	},
	regExpCheck: function (reg, str) {
		if (reg.test(str)) {
			return true;
		} else {
			return false;
		}
	},
	init: function (parameter) {

		MyForm.parameter = parameter;

		MyForm.fixStyle('.form-input input');
		MyForm.fixStyle('.form-selector select');

		var forms = document.querySelectorAll('form');
		for (var i = 0; i < forms.length; i ++) {
			forms[i].onsubmit = MyForm.checkForms;
		}
	},
	fixStyle: function (selector) {
		var nodes = document.querySelectorAll(selector);
		for (var i = 0; i < nodes.length; i ++) {
			var width = nodes[i].parentNode.offsetWidth - 24 - 1;
			width -= document.querySelector('[for=' + nodes[i].id + ']').offsetWidth;
			nodes[i].style.width = width + 'px';
		}
	},
	preprocessingTextarea: function () {
		var nodes = document.querySelectorAll('.form-textarea p');
		for (var i = 0; i < nodes.length; i ++) {
			nodes[i].parentNode.querySelector('input[type=hidden]').value = nodes[i].textContent;
		}
	},
	checkForms: function () {
		MyForm.clearHint();

		var parameter = MyForm.parameter
		for (key in parameter) {
			var str = null;
			if (document.querySelector(key).tagName === 'P') {
				str = document.querySelector(key).textContent;
				document.querySelector(key + '-textarea').textContent = str;
			} else {
				str = document.querySelector(key).value;
			}

			//检查是否为空
			if(parameter[key].beNull !== true) {
				if(MyForm.checkNull(str)) {
					MyForm.addHint(key, parameter[key].hintTitle + '不能为空');
					return false;
				}
			}

			//检查正确性
			if(typeof(parameter[key].condition) === 'number') {
				if(!MyForm.checkLength(str, parameter[key].condition)) {
					MyForm.addHint(key, parameter[key].hintTitle + '不能超过' + parameter[key].condition + '字');
					return false;
				}
			} else if (typeof(parameter[key].condition) === 'function') {
				if(!parameter[key].condition(str)) {
					MyForm.addHint(key, parameter[key].hintTitle + '不正确');
					return false;
				}
			}
		}
	},
}