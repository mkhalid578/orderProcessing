$(document).ready(function(){

		document.getElementById("digital-order-form").style.display ="block";
    UpdateProfileDataforform();
    UpdateProfileData();

       $('li a').click(function() {
            $('li a').removeClass('active');
            $(this).addClass('active');
            var v_href = $(this).attr('href');

            if (v_href == "#!digital-order-form"){

              	document.getElementById("digital-order-form").style.display ="block";
              	document.getElementById("order-data").style.display ="none";
              	document.getElementById("profile").style.display ="none";
              	document.getElementById("user-logout").style.display ="none";

            } else if(v_href == "#!order-data") {

              	document.getElementById("digital-order-form").style.display ="none";
              	document.getElementById("order-data").style.display ="block";
              	document.getElementById("profile").style.display ="none";
              	document.getElementById("user-logout").style.display ="none";
                   $("#placed-order-table").DataTable().draw();

            } else if(v_href == "#!profile") {

              	document.getElementById("digital-order-form").style.display ="none";
              	document.getElementById("order-data").style.display ="none";
              	document.getElementById("profile").style.display ="block";
              	document.getElementById("user-logout").style.display ="none";
 
            } else if(v_href == "#!user-logout") {

              	document.getElementById("digital-order-form").style.display ="none";
              	document.getElementById("order-data").style.display ="none";
              	document.getElementById("profile").style.display ="none";
              	document.getElementById("user-logout").style.display ="block";
            }
       });




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
                                      "order-use-reason" : $("#order-use-reason").val()
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
                          $("#order-item-name").val() = "";
                          $("#order-item-detail").val() = "";
                          $("#order-item-quentities").val() = "";
                          $("#order-from-where").val() = "";
                          $("#order-time-period").val() = "";
                          $("#order-use-reason").val() = "";
  
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





















       var placed_order_table =
            $("#placed-order-table").DataTable(
                  { "ajax": {
   														 "url": "data/order-process/orderlist/",
    													 "dataSrc": function ( json ) {
    																				  for ( var i=0, ien=json.data.length ; i<ien ; i++ ) {
        																							json.data[i][0] = '<a href="/message/'+json.data[i][0]+'>View message</a>';
      																				}
      																				return json.data;
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
                         {"title" : "PlaceOrderData"},
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

            placed_order_table.columns( [ 0, 3, 4, 7, 9, 10, 12, 14, 15, 16, 17, 18] )
                             .visible( false, true );

            // adjust column sizing and redraw
            placed_order_table.columns.adjust().draw( false );
            placed_order_table.draw(); // redraw

            document.getElementsByClassName("dataTables_scroll")[0].style.overflow = "scroll";
            document.getElementsByClassName("dataTables_scrollHead")[0].style.overflow = "";
            document.getElementsByClassName("dataTables_scrollBody")[0].style.overflow = "";


           placed_order_table.row.add([
                  "11",
                  "vibhuti",
                  "patel",
                  "vibhuti_patel1@student.uml.edu",
                  "student",
                  "Electrical engineering",
                  "grounding-cabel",
                  "xyz detail",
                  "2counts",
                  "amazon.com",
                  "2-3days",
                  "EE capsote project",
                  "Please, order ASAP",
                  "order-placed",
                  "USPS",
                  "abcd99999999",
                  "www.usps.com",
                  "3-23-2017",
                  "3-23-2017"
                        ]).draw();





           $('#placed-order-table tbody').on( 'click', 'tr', function () {
              if ( $(this).hasClass('selected') ) {
                  $(this).removeClass('selected');
              }
              else {
                  placed_order_table.$('tr.selected').removeClass('selected');
                  $(this).addClass('selected');
                  console.log(placed_order_table.row('.selected').data());
                  var selected_order_detail = placed_order_table.row('.selected').data();
                  displayorderdata(selected_order_detail);

                  $d("#OrderItemDialog").dialog('open').scrollTop(0);
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
                       "Use/Reason :               " + selected_order_detail[11] + "\n \n" +
                       "PlaceOrderData :           " + selected_order_detail[12] + "\n \n" ;

              $("#order-status-detail").val(selected_order_detail[13]);

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
                      document.getElementById("order-status-detail").disabled = false;
                  },
                  'Save': function() {
                      $d(this).dialog('close');
                 }
               },
               autoOpen : false
           });


           





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

});

