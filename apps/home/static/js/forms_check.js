$(function() {
	/*placeholder 效果*/
	(function() {
		$('.input-xlarge').focus(function () {
			this.placeText = $(this).attr('placeholder');
			$(this).removeAttr('placeholder')
        }).blur(function () {
        	$(this).attr('placeholder', this.placeText);
        });

		function isEmail(str){
			var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
			return reg.test(str);
		}

		function check_error() {
			if ($('.input-xlarge').hasClass('highlight2')){
				$('#regButton').attr('disabled', true);
				return
			}else if ($('.msgSpan').hasClass('fail')){
				$('#regButton').attr('disabled', true);
				return
			}
			$('#regButton').attr('disabled', false);
        }

        function check_error2() {
			if ($('#regName').hasClass('highlight2') || $('#regNameMsg').hasClass('fail')){
				$('#regButton').attr('disabled', true);
				return
			}else if ($('#regEmail').hasClass('highlight2') || $('#regEmailMsg').hasClass('fail')){
				$('#regButton').attr('disabled', true);
				return
			}
			$('#regButton').attr('disabled', false);
        }


		// 自动验证用户名
		$('#regName').focus(function() {
			$(this).removeClass('highlight2');
			$('#regNameMsg').removeClass('succeed').removeClass('fail').text('');
			check_error()
		}).blur(function() {
			if ($(this).val().length >= 4 && $(this).val().length <= 20) {
				$.ajax({
					url: '/api/ck_un',
					type: 'GET',
					data: 'username=' + $('#regName').val(),
					success: function(data) {
						if (data.status == 'success') {
							$('#regName').removeClass('highlight2');
							$('#regNameMsg').addClass('succeed').text('该用户名可以使用');
							check_error()
						} else {
							$('#regName').removeClass('highlight2').addClass('highlight2');
							$('#regNameMsg').removeClass('succeed').addClass('fail').text('该用户名已被使用，请重新输入。');
							$('#regButton').attr('disabled', true);
						}
					}
				});
			}
			else {
				$('#regName').removeClass('highlight2').addClass('highlight2');
				$('#regNameMsg').addClass('fail').text('用户名长度只能在4-20位字符之间');
				$('#regButton').attr('disabled', true);

			}
		});


		//自动验证邮箱
		$('#regEmail').focus(function() {
			$(this).removeClass('highlight2');
			$('#regEmailMsg').removeClass('succeed').removeClass('fail').text('');
			check_error()
		}).blur(function() {
			if (isEmail($(this).val())) {
				$.ajax({
					url: '/api/ck_email',
					type: 'GET',
					data: 'email=' + $('#regEmail').val(),
					success: function(data) {
						if (data.status == 'success') {
							$('#regEmail').removeClass('highlight2');
							$('#regEmailMsg').addClass('succeed').text('该邮箱可以使用');
							check_error()
						} else {
							$('#regEmail').removeClass('highlight2').addClass('highlight2');
							$('#regEmailMsg').removeClass('succeed').addClass('fail').text('该邮箱已被使用，请重新输入');
							$('#regButton').attr('disabled', true);
						}
					}
				});
			}
			else {
				$('#regEmail').removeClass('highlight2').addClass('highlight2');
				$('#regEmailMsg').addClass('fail').text('请输入正确的邮箱');
				$('#regButton').attr('disabled', true);

			}
		});


		//验证密码
		$('#regPwd').focus(function() {
		$('#regPwd').removeClass('highlight2');
		$('#regPwdMsg').removeClass('fail').text('');
		check_error2()
	}).blur(function() {
		if ($(this).val().length >= 6 && $(this).val().length <= 20) {
			if ($(this).val() == $('#regPwd2').val()) {
				$('#regPwd').removeClass('highlight2');
				$('#regPwd2').removeClass('highlight2');
				$('#regPwdMsg').removeClass('fail').text('');
				$('#regPwdMsg2').removeClass('fail').text('');
				check_error()
			} else {
				$('#regPwd').removeClass('highlight2').addClass('highlight2');
				$('#regPwd2').removeClass('highlight2').addClass('highlight2');
				$('#regPwdMsg').addClass('fail').text('两次输入密码不一致');
				$('#regPwdMsg2').addClass('fail').text('两次输入密码不一致');
				$('#regButton').attr('disabled', true);
			}
		}
		else {
			$('#regPwd').removeClass('highlight2').addClass('highlight2');
			$('#regPwdMsg').addClass('fail').text('密码长度只能在6-20位字符之间');
			$('#regButton').attr('disabled', true);
		}
	});

		$('#regPwd2').focus(function() {
		$('#regPwd2').removeClass('highlight2');
		$('#regPwdMsg2').removeClass('fail').text('');
		check_error2()
	}).blur(function() {
		if ($(this).val().length >= 6 && $(this).val().length <= 20) {
			if ($(this).val() == $('#regPwd').val()) {
				$('#regPwd').removeClass('highlight2');
				$('#regPwd2').removeClass('highlight2');
				$('#regPwdMsg').removeClass('fail').text('');
				$('#regPwdMsg2').removeClass('fail').text('');
				check_error()
			} else {
				$('#regPwd').removeClass('highlight2').addClass('highlight2');
				$('#regPwd2').removeClass('highlight2').addClass('highlight2');
				$('#regPwdMsg').addClass('fail').text('两次输入密码不一致');
				$('#regPwdMsg2').addClass('fail').text('两次输入密码不一致');
				$('#regButton').attr('disabled', true);
			}
		}
		else {
			$('#regPwd2').removeClass('highlight2').addClass('highlight2');
			$('#regPwdMsg2').addClass('fail').text('密码长度只能在6-20位字符之间');
			$('#regButton').attr('disabled', true);
		}
	});

		$('#reg_form').submit(function () {
	$.ajax({
        type: "POST",
        data: $('#reg_form').serialize(),
        url: "/users/register/",
        cache: false,
        dataType: "json",
        success: function(json){
        	var errors = json.errors;
            if(json.status == 'success'){
				location.replace(location.href);
            }else{
				$('#signUpStatus').text('SIGN UP');
				for(error in errors){
					if (error == 'username'){
						$('#regName').removeClass('highlight2');
						$('#regNameMsg').removeClass('fail');
						$('#regName').addClass('highlight2');
						$('#regNameMsg').addClass('fail').text(errors[error]);
					}
					else if (error == 'email'){
						$('#regEmail').removeClass('highlight2');
						$('#regEmailMsg').removeClass('fail');
						$('#regEmail').addClass('highlight2');
						$('#regEmailMsg').addClass('fail').text(errors[error]);
					};
					if (error == 'password'){
						$('#regPwd').removeClass('highlight2');
						$('#regPwdMsg').removeClass('fail');
						$('#regPwd').addClass('highlight2');
						$('#regPwdMsg').addClass('fail').text(errors[error]);
					};
					if (error == 'password2'){
						$('#regPwd2').removeClass('highlight2');
						$('#regPwdMsg2').removeClass('fail');
						$('#regPwd2').addClass('highlight2');
						$('#regPwdMsg2').addClass('fail').text(errors[error]);
					};
				}

                tip.text('邮箱或者密码错误，请重试');
            };
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            tip.text("登录出错，请重试 "+errorThrown);
        }
    });
	$('#signUpStatus').text('REGISTERING...')
    return false;
});

	})();
});


// 验证码刷新与动态验证
$(function(){
$('.captcha').css({
	'cursor': 'pointer'
})
// # ajax 刷新
$('.captcha').click(function(){
	console.log('click');
	 $.getJSON("/captcha/refresh/",
			  function(result){
		 $('.captcha').attr('src', result['image_url']);
		 $('#id_captcha_0').val(result['key'])
	  });


});

// 动态验证

$('#id_captcha_1').blur(function(){  // #id_captcha_1为输入框的id，当该输入框失去焦点是触发函数
	json_data={
		'response':$('#id_captcha_1').val(),  // 获取输入框和隐藏字段id_captcha_0的数值
		'hashkey':$('#id_captcha_0').val()
	}
	$.getJSON('/ajax_val', json_data, function(data){ //ajax发送
		$('#captcha_status').remove();
		if(data['status']){ //status返回1为验证码正确， status返回0为验证码错误， 在输入框的后面写入提示信息
			$('#id_captcha_1').after('<span id="captcha_status" style="color:blue">*验证码正确</span>')
		}else{
			 $('#id_captcha_1').after('<span id="captcha_status" style="color:red">*验证码错误</span>')
		}
	});

});


})

