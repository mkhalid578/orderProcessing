$(document).ready(function(){

		document.getElementById("digital-order-form").style.display ="block";
 
    // this use for updating data in form after user edit data in profile tab
    var ProfileDataEdited = false;
    UpdateProfileDataforform();
    UpdateProfileData();
    var orderupdateVar;  // updating order table using interval


       $('li a').click(function() {
            $('li a').removeClass('active');
            $(this).addClass('active');
            var v_href = $(this).attr('href');

            if (v_href == "#!digital-order-form"){

              	document.getElementById("digital-order-form").style.display ="block";
              	document.getElementById("order-data").style.display ="none";
              	document.getElementById("profile").style.display ="none";
              	document.getElementById("user-logout").style.display ="none";
                if (ProfileDataEdited == true){
                    UpdateProfileDataforform();
                    ProfileDataEdited = false;
                }
                clearTimeout(orderupdateVar);
            } else if(v_href == "#!order-data") {

              	document.getElementById("digital-order-form").style.display ="none";
              	document.getElementById("order-data").style.display ="block";
              	document.getElementById("profile").style.display ="none";
              	document.getElementById("user-logout").style.display ="none";
                $("#placed-order-table").DataTable().draw();
                orderupdateVar = setInterval( UpdateOrderDataPriodically, 30000 );

            } else if(v_href == "#!profile") {

              	document.getElementById("digital-order-form").style.display ="none";
              	document.getElementById("order-data").style.display ="none";
              	document.getElementById("profile").style.display ="block";
              	document.getElementById("user-logout").style.display ="none";
                clearTimeout(orderupdateVar);
 
            } else if(v_href == "#!user-logout") {

              	document.getElementById("digital-order-form").style.display ="none";
              	document.getElementById("order-data").style.display ="none";
              	document.getElementById("profile").style.display ="none";
              	document.getElementById("user-logout").style.display ="block";
                clearTimeout(orderupdateVar);
            }
       });



// **********************************************************************************************************************
        // Digital order form data

        function UpdateProfileDataforform() {
                // Update data about logged user data from database
                $.ajax({
											    type : "GET",
											    url : "/load_profile_data_for_form",
											    success: function(result) {
                              var obj = JSON.parse(result)
                              if ((obj.status) == 'OK'){
                              		$("#order-first-name").val(obj.firstName) 
                              		$("#order-last-name").val(obj.lastName) 
                              		$("#order-email-id").val(obj.email) 
                              		$("#order-user-id").val(obj.userId) 
                              		$("#order-employ-position").val(obj.position) 
                              		$("#order-department").val(obj.deptarment)
                              } else {
                                 console.log("Logged In user data is not found!")
                              		$("#current-employ-first-name").val(" ") 
                              		$("#current-employ-last-name").val(" ") 
                              		$("#current-employ-email-id").val(" ") 
                              		$("#current-employ-user-id").val(" ") 
                              		$("#current-employ-password").val(" ") 
                              		$("#current-employ-position").val(" ") 
                              		$("#current-employ-department").val(" ")
                              } 
											    },
                          error: function(error) {
                              console.log(error);
                          }
								});
        }

        document.getElementById("submit-new-order-bt").onclick = function() {Addneworder()};
           function Addneworder() {
                    
                    if ((($("#order-item-name").val()).trim() == "") ||
                        (($("#order-item-quentities").val()).trim() == "") ||
                        (($("#order-from-where").val()).trim() == "") ||
                        (($("#order-time-period").val()).trim() == "") ||
                        (($("#order-use-reason").val()).trim() == "")){
                           $d("#NewOrderItemErrorDialog").dialog("open");
                    } else {
                        var obj_data = {
                                      "order-first-name" : $("#order-first-name").val(),
                                      "order-last-name" : $("#order-last-name").val(),
                                      "order-email-id" : $("#order-email-id").val(),
                                      "order-employ-position" : $("#order-employ-position").val(),
                                      "order-department" : $("#order-department").val(),
                                      "order-item-name" : $("#order-item-name").val(),
                                      "order-item-detail" : $("#order-item-detail").val(),
                                      "order-item-quentities" : $("#order-item-quentities").val(),
                                      "order-from-where" : $("#order-from-where").val(),
                                      "order-time-period" : $("#order-time-period").val(),
                                      "order-use-reason" : $("#order-use-reason").val(),
                                      "order-status" : "approval-pending"
                                   }
                        var new_order_data = JSON.stringify(obj_data);
                        $.ajax({
                            type : "GET",
                            url : "load_new_order_data",
                            data : { key : new_order_data}, 
                            dataType : 'json',
                            contentType : 'application/json; charset=utf-8',
                            success : function(data) {
                               console.log(data);
                            }
                        });
                        
                       // clear form
                          $("#order-item-name").val("");
                          $("#order-item-detail").val("");
                          $("#order-item-quentities").val("");
                          $("#order-from-where").val("");
                          $("#order-time-period").val("");
                          $("#order-use-reason").val("");
  
                    }
                    

           }

           // use $d instead of $ because to avoid conflict of jquery js libraries of different version.
           $d("#NewOrderItemErrorDialog").dialog({
               modal : true,
               closeOnEscape : true,
               maxHeight: 200,
               width : 300,
               maxWidth: 300,
               position: { my: "center", at: "center", of: window },
               buttons : {
                  'OK': function() {
                      $d(this).dialog('close');
                 }
               },
               autoOpen : false
           });



// **********************************************************************************************************************


       var placed_order_table =
            $("#placed-order-table").DataTable(
                  { "ajax": {
   														 "url": "/data/order-process/orderlist",
    													 "dataSrc": function (result) {
                                              var obj = [];
    																				  for ( var i=0; i < (result.status_data).length ; i++ ) {
                                                    obj.push(JSON.parse((result.status_data)[i]));
      																				}
      																			  upload_order_data_table(obj);
    																			}
  													},
                    "columns" : [ {"title" : "ItemNumber"},
                    	   {"title" : "First-Name"},
                      	 {"title" : "Last-Name"},
       	      	         {"title" : "Email-Id"},
        	               {"title" : "Position"},
          	             {"title" : "Department"},
            	           {"title" : "Item-Name"},
                         {"title" : "Item-Detail"},
                         {"title" : "Item-Quentities"},
                         {"title" : "From-Where"},
                         {"title" : "Time-Period"},
                         {"title" : "Use/Reason"},
                         {"title" : "Placed-Order-Date"},
                         {"title" : "Order-Status"},
                         {"title" : "Shipment-Company"},
                         {"title" : "Tracking-Number"},
                         {"title" : "Tracking-Webside"},
                         {"title" : "Expected-Arriving-Date"},
                         {"title" : "Arrived-Date"}],

                  	"info" : false,
                  	"ordering": true,
                  	"scrollX" : "500px",
                  	"scrollCollapse" : false,
                  	"searching" : false});

            placed_order_table.columns( [ 0, 3, 4, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18] )
                             .visible( false, true );

            // adjust column sizing and redraw
            placed_order_table.columns.adjust().draw( false );
            placed_order_table.draw(); // redraw

            document.getElementsByClassName("dataTables_scroll")[0].style.overflow = "scroll";
            document.getElementsByClassName("dataTables_scrollHead")[0].style.overflow = "";
            document.getElementsByClassName("dataTables_scrollBody")[0].style.overflow = "";


      		 function upload_order_data_table(obj){
                 for(var i = 0; i < obj.length; i++){  
                    placed_order_table.row.add([
                                  obj[i]["ItemNumber"],
                                  obj[i]["First-Name"],
                                  obj[i]["Last-Name"],
                     	      	    obj[i]["Email-Id"],
        	                        obj[i]["Position"],
                        	        obj[i]["Department"],
            	                    obj[i]["Item-Name"],
                                  obj[i]["Item-Detail"],
                                  obj[i]["Item-Quentities"],
                                  obj[i]["From-Where"],
                                  obj[i]["Time-Period"],
                                  obj[i]["Use/Reason"],
                                  obj[i]["Placed-Order-Date"],
                                  obj[i]["Order-Status"],
                                  obj[i]["Shipment-Company"],
                                  obj[i]["Tracking-Number"],
                                  obj[i]["Tracking-Webside"],
                                  obj[i]["Expected-Arriving-Date"],
                                  obj[i]["Arrived-Date"]
                             ])
                 }
                 placed_order_table.draw(false); // redraw
           }

           // this var is used for updating data in database for item order
           var selected_item_id_number;
           $('#placed-order-table tbody').on( 'click', 'tr', function () {
              if ( $(this).hasClass('selected') ) {
                  $(this).removeClass('selected');
              }
              else {
                  placed_order_table.$('tr.selected').removeClass('selected');
                  $(this).addClass('selected');
                  var selected_order_detail = placed_order_table.row('.selected').data();
                  displayorderdata(selected_order_detail);
                  selected_item_id_number = selected_order_detail[0];

                  $d("#OrderItemDialog").dialog('open').scrollTop(0);
                  if (document.getElementById("current-employ-worker").checked){
                        // first is "edit" button and second is "save" button and third is delete
                        document.getElementsByClassName("ui-button-text-only")[1].setAttribute("style","visibility : hidden;");
                        document.getElementsByClassName("ui-button-text-only")[2].setAttribute("style","visibility : hidden;");
                        document.getElementsByClassName("ui-button-text-only")[3].setAttribute("style","visibility : hidden;");
                  } else {
                         //editing authority for order handler/manager
                  }
              }
           } );

            
           function displayorderdata(selected_order_detail) {

              var order_person_detail_row = "First-Name : " + selected_order_detail[1] + "           " +
                       "Last-Name : " + selected_order_detail[2] + "\n" +
                       "Email-Id : " + selected_order_detail[3] + "\n" +
                       "Position : " + selected_order_detail[4] + "\n" +
                       "Department : " + selected_order_detail[5] + "\n" ;


              var order_item_detail_row =
                       "Item-Name :                " + selected_order_detail[6] + "\n \n" +
                       "Item-Detail :              " + selected_order_detail[7] + "\n \n" +
                       "Item-Quentities :          " + selected_order_detail[8] + "\n \n" +
                       "From-Where :               " + selected_order_detail[9] + "\n \n" +
                       "Time-Period :              " + selected_order_detail[10] + "\n \n" +
                       "Use/Reason :               " + selected_order_detail[11] + "\n \n";

              $("#order-status-detail").val(selected_order_detail[13]);

              $("#item-detail-placed-order-date").val(selected_order_detail[12]);
              $("#item-detail-shipment-company").val(selected_order_detail[14]);
              $("#item-detail-tracking-number").val(selected_order_detail[15]);
              $("#item-detail-tracking-website").val(selected_order_detail[16]);
              $("#item-detail-expected-arriving-date").val(selected_order_detail[17]);
              $("#item-detail-arrived-date").val(selected_order_detail[18]);

              // $('#placed-order-item-detail-dialogtext').html(placed_order_item_detail_row);
              $('#order-item-detail-dialogtext').html(order_item_detail_row);
              $('#order-person-detail-dialogtext').html(order_person_detail_row);

           }


           // use $d instead of $ because to avoid conflict of jquery js libraries of different version.
           $d("#OrderItemDialog").dialog({
               modal : true,
               closeOnEscape : true,
               maxHeight: 600,
               width : 900,
               maxWidth: 900,
               position: { my: "top", at: "top", of: window },
               buttons : {
                  'Edit': function() {
                      //do something
                      if (document.getElementById("current-employ-order-handler").checked){
                           var order_tracking_data_inputs = document.getElementById('placed-order-item-detail-dialogtext')
                                                                   .getElementsByTagName('input');
                           for (i = 0; i < order_tracking_data_inputs.length; i++) {
                                     order_tracking_data_inputs[i].removeAttribute("readonly");
                           }
                           document.getElementById("order-status-detail").disabled = false;
                      } else if (document.getElementById("current-employ-manager").checked){
                           document.getElementById("order-status-detail").disabled = false;
                           document.getElementById("item-delete-donot-approved").disabled = false;
                      } else {
                         //not editing authority for employ
                      }
                  },
                  'Save': function() {

                      if (document.getElementById("current-employ-order-handler").checked){
                           var obj_data = {
                                      "order-item-id" : selected_item_id_number,
                                      "order-status" : $("#order-status-detail").val(),
                                      "placed-order-date" : $("#item-detail-placed-order-date").val(),
                                      "shipment-company" : $("#item-detail-shipment-company").val(),
                                      "tracking-number" : $("#item-detail-tracking-number").val(),
                                      "tracking-website" : $("#item-detail-tracking-website").val(),
                                      "expected-arriving-date" : $("#item-detail-expected-arriving-date").val(),
                                      "arrived-date" : $("#item-detail-arrived-date").val()
                                      }
                           var edited_order_data = JSON.stringify(obj_data);
                           $.ajax({
                               type : "GET",
                               url : "load_edited_order_data",
                               data : { key : edited_order_data}, 
                               dataType : 'json',
                               contentType : 'application/json; charset=utf-8',
                               success : function(result) {
                                   var obj = [];
                                      for ( var i=0; i < (result.status_data).length ; i++ ) {
                                              obj.push(JSON.parse((result.status_data)[i]));
                                      }
                                    
                                   placed_order_table.rows().remove();
                                   upload_order_data_table(obj);
                               }
                           });
                      } else if (document.getElementById("current-employ-manager").checked){
                           var obj_data = {
                                      "order-item-id" : selected_item_id_number,
                                      "order-status" : $("#order-status-detail").val()}
                           var edited_order_status_data = JSON.stringify(obj_data);
                           $.ajax({
                               type : "GET",
                               url : "load_edited_order_status_data",
                               data : { key : edited_order_status_data}, 
                               dataType : 'json',
                               contentType : 'application/json; charset=utf-8',
                               success : function(result) {
                                   var obj = [];
                                      for ( var i=0; i < (result.status_data).length ; i++ ) {
                                              obj.push(JSON.parse((result.status_data)[i]));
                                      }
                                    
                                   placed_order_table.rows().remove();
                                   upload_order_data_table(obj);
                               }
                           });
                      } else {
                         //not editing authority for employ
                      }

                      // updated database
                      document.getElementById("order-status-detail").disabled = true;
                      $d(this).dialog('close');
                      var order_tracking_data_inputs = document.getElementById('placed-order-item-detail-dialogtext')
                                                                   .getElementsByTagName('input');
                               for (i = 0; i < order_tracking_data_inputs.length; i++) {
                                     order_tracking_data_inputs[i].setAttribute("readonly","");
                               }
                      document.getElementById("item-delete-donot-approved").setAttribute("readonly","");
                      document.getElementById("item-delete-donot-approved").checked = false;
                 },
                 'Delete': function() {
                      //do something
                      if (document.getElementById("current-employ-manager").checked &&
                          document.getElementById("item-delete-donot-approved").checked){
                           var obj_data = {
                                      "order-item-id" : selected_item_id_number}
                           var deleted_order_data = JSON.stringify(obj_data);
                           $.ajax({
                               type : "GET",
                               url : "load_deleted_order_data",
                               data : { key : deleted_order_data}, 
                               dataType : 'json',
                               contentType : 'application/json; charset=utf-8',
                               success : function(result) {
                                   var obj = [];
                                      for ( var i=0; i < (result.status_data).length ; i++ ) {
                                              obj.push(JSON.parse((result.status_data)[i]));
                                      }
                                    
                                   placed_order_table.rows().remove();
                                   upload_order_data_table(obj);
                               }
                           });
                      } else {
                         //not deleting authority for employ and order handler
                      }
                      document.getElementById("order-status-detail").disabled = true;
                      $d(this).dialog('close');
                      var order_tracking_data_inputs = document.getElementById('placed-order-item-detail-dialogtext')
                                                                   .getElementsByTagName('input');
                               for (i = 0; i < order_tracking_data_inputs.length; i++) {
                                     order_tracking_data_inputs[i].setAttribute("readonly","");
                               }
                      document.getElementById("item-delete-donot-approved").disabled = true;
                      document.getElementById("item-delete-donot-approved").checked = false;
                  },
               },
               autoOpen : false
           });

        function UpdateOrderDataPriodically() {
                // Update order data from database at every mint
                // setInterval( UpdateOrderDataPriodically, 60000 );
                placed_order_table.rows().remove();
                placed_order_table.ajax.reload( null, false ); // user paging is not reset on reload;
        }
           



// **********************************************************************************************************************
       // profile data

           function UpdateProfileData() {
                // Update data about logged user data from database
                $.ajax({
											    type : "GET",
											    url : "/load_profile_data",
											    success: function(result) {
                              var obj = JSON.parse(result)
                              if ((obj.status) == 'OK'){
                              		$("#current-employ-first-name").val(obj.firstName) 
                              		$("#current-employ-last-name").val(obj.lastName) 
                              		$("#current-employ-email-id").val(obj.email) 
                              		$("#current-employ-user-id").val(obj.userId) 
                              		$("#current-employ-password").val(obj.password) 
                              		$("#current-employ-position").val(obj.position) 
                              		$("#current-employ-department").val(obj.deptarment)

                                  var order_authority_data = obj.order_authority;
                                  if (order_authority_data == "order-handler"){
                                      document.getElementById("current-employ-order-handler").checked = true;
                                  } else if (order_authority_data == "manager"){
                                      document.getElementById("current-employ-manager").checked = true;
                                  } else {
                                      document.getElementById("current-employ-worker").checked = true;
                                  }

                              } else {
                                 console.log("Logged In user data is not found!")
                              		$("#current-employ-first-name").val(" ") 
                              		$("#current-employ-last-name").val(" ") 
                              		$("#current-employ-email-id").val(" ") 
                              		$("#current-employ-user-id").val(" ") 
                              		$("#current-employ-password").val(" ") 
                              		$("#current-employ-position").val(" ") 
                              		$("#current-employ-department").val(" ")
                                  document.getElementById("current-employ-worker").checked = true;
                              } 
											    },
                          error: function(error) {
                              console.log(error);
                          }
								});

           }

        document.getElementById("allow-profile-edit-bt").onclick = function() {AllowProfileEditing()};
           function AllowProfileEditing() {
               var profile_data_inputs = document.getElementById('profile').getElementsByTagName('input');
 	              for (i = 0; i < profile_data_inputs.length; i++) {
                  // USR COULD NOT EDIT USER_ID
                  if (i != 3){
                    profile_data_inputs[i].removeAttribute("readonly");
                  }
							  }
                document.getElementById("submit-current-employ-account-btn").disabled = false;
                document.getElementById("cancel-current-employ-account-btn").disabled = false;

           }


        document.getElementById("cancel-current-employ-account-btn").onclick = function() {
                UpdateProfileData();
                var profile_data_inputs = document.getElementById('profile').getElementsByTagName('input');
                for (i = 0; i < profile_data_inputs.length; i++) {
                  if (i != 3){
                    profile_data_inputs[i].setAttribute("readonly","");
                  }
                }
                document.getElementById("submit-current-employ-account-btn").disabled = true;
                document.getElementById("cancel-current-employ-account-btn").disabled = true;
            
        };

        document.getElementById("submit-current-employ-account-btn").onclick = function() {UpdateProfileEditing()};
           function UpdateProfileEditing() {

                    if ((($("#current-employ-first-name").val()).trim() == "") ||
                        (($("#current-employ-last-name").val()).trim() == "") ||
                        (($("#current-employ-email-id").val()).trim() == "") ||
                        (($("#current-employ-user-id").val()).trim() == "") ||
                        (($("#current-employ-password").val()).trim() == "") ||
                        (($("#current-employ-position").val()).trim() == "") ||
                        (($("#current-employ-department").val()).trim() == "")){
                           $d("#EditedProfileErrorDialog").dialog("open");
                           UpdateProfileData();
                    } else {
                          var order_authority_data = "employ";
                          if (document.getElementById("current-employ-order-handler").checked){
                              order_authority_data = $("#current-employ-order-handler").val();
                          } else if (document.getElementById("current-employ-manager").checked){
                              order_authority_data = $("#current-employ-manager").val();
                          } else {
                              order_authority_data = $("#current-employ-worker").val();
                          }

                          var obj_data = {
                                      "first-name" : $("#current-employ-first-name").val(),
                                      "last-name" : $("#current-employ-last-name").val(),
                                      "email-id" : $("#current-employ-email-id").val(),
                                      "user-id" : $("#current-employ-user-id").val(),
                                      "password" : $("#current-employ-password").val(),
                                      "position" : $("#current-employ-position").val(),
                                      "department" : $("#current-employ-department").val(),
                                      "order-authority" : order_authority_data
                                   }
                        var edited_profile_data = JSON.stringify(obj_data);
                        $.ajax({
                            type : "GET",
                            url : "load_edited_profile_data",
                            data : { key : edited_profile_data}, 
                            dataType : 'json',
                            contentType : 'application/json; charset=utf-8',
                            success : function(data) {
                               console.log(data);
                            }
                        });
                        ProfileDataEdited = true;
                    }

               var profile_data_inputs = document.getElementById('profile').getElementsByTagName('input');
 	              for (i = 0; i < profile_data_inputs.length; i++) {
                  if (i != 3){
                    profile_data_inputs[i].setAttribute("readonly","");
                  }
							  }
                document.getElementById("submit-current-employ-account-btn").disabled = true;
                document.getElementById("cancel-current-employ-account-btn").disabled = true;

        }

        // use $d instead of $ because to avoid conflict of jquery js libraries of different version.
           $d("#EditedProfileErrorDialog").dialog({
               modal : true,
               closeOnEscape : true,
               maxHeight: 200,
               width : 300,
               maxWidth: 300,
               position: { my: "center", at: "center", of: window },
               buttons : {
                  'OK': function() {
                      $d(this).dialog('close');
                 }
               },
               autoOpen : false
           });

});  // END of File

