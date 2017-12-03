//select
function getRadioValue(name){
	var val="";
	$("input[name='"+name+"']").each(function(){
		if($(this).attr("checked")){
			val=$(this).val();
		}
	});
	return val;
}
//select
function getCheckboxValue(name){
	var val="";
	$("input[name='"+name+"']").each(function(){
		if($(this).attr("checked")){
			if(val==""){
				val=$(this).val();
			}else{
				val=val+","+$(this).val();
			}

		}
	});
	return val;
}

function submitWkXtAll(){
	var allmsg="";
	$("li[name='xt']").each(function(){
		var tag=$(this).attr("tag");
		var pid=$(this).attr("id").split("_")[1];
		if(tag=="1"||tag=="4"){
			var type=parseInt($(this).attr("tagtype"));
			if(type==0){
				var name="tk_"+pid;
				var msg="";
				//填空
				$("input[name='"+name+"']").each(function(){
					var val=$(this).val();
					if(val==""){
						msg="";
						return;
					}else{
						if(msg==""){
							msg=val;
						}else{
							msg=msg+"&,&"+val;
						}
					}

				});
			}else if(type==1){
				var name="dx_"+pid;
				msg=getRadioValue(name);
			}else if(type==2){
				var name="mx_"+pid;
				msg=getCheckboxValue(name);
			}else if(type==3){
				var name="pd_"+pid;
				msg=getRadioValue(name);
			}
			if(msg!=""){
				if(allmsg==""){
					allmsg=pid+"&=&"+msg;
				}else{
					allmsg=allmsg+"&;&"+pid+"&=&"+msg;
				}
			}
		}
	});
	if(allmsg==""){
		return;
	}else{
		return allmsg;
	}
}
