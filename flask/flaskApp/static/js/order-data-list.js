$(document).ready(function(){

		document.getElementById("digital-order-form").style.display ="block";

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
                UpdateProfileData();
 
            } else if(v_href == "#!user-logout") {

              	document.getElementById("digital-order-form").style.display ="none";
              	document.getElementById("order-data").style.display ="none";
              	document.getElementById("profile").style.display ="none";
              	document.getElementById("user-logout").style.display ="block";
            }
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
											        console.log("vibhuti");
											        console.log(result);
                              var obj = JSON.parse(result)
                              if ((obj.status) == 'OK'){
                              		$("#current-employ-first-name").val(obj.firstName) 
                              		$("#current-employ-last-name").val(obj.lastName) 
                              		$("#current-employ-email-id").val(obj.email) 
                              		$("#current-employ-user-id").val(obj.userId) 
                              		$("#current-employ-password").val(obj.password) 
                              		$("#current-employ-position").val(obj.position) 
                              		$("#current-employ-department").val(obj.deptarment)
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

        document.getElementById("allow-profile-edit-bt").onclick = function() {AllowProfileEditing()};
           function AllowProfileEditing() {
               var profile_data_inputs = document.getElementById('profile').getElementsByTagName('input');
 	              for (i = 0; i < profile_data_inputs.length; i++) {
                    profile_data_inputs[i].removeAttribute("readonly");
							  }
                document.getElementById("current-employ-order-handler").disabled = false;
                document.getElementById("current-employ-manager").disabled = false;
                document.getElementById("current-employ-worker").disabled = false;
                document.getElementById("submit-current-employ-account-btn").disabled = false;

           }


        document.getElementById("submit-current-employ-account-btn").onclick = function() {UpdateProfileEditing()};
           function UpdateProfileEditing() {

								console.log("vibhuti submit bt");
                /* 
                $.ajax({
											    type : "POST",
											    url : "/update_profile_data",
											    success: function(result) {
											        console.log("vibhuti");
											        console.log(result);
                              var obj = JSON.parse(result)
											        console.log(obj.status);
                              if ((obj.status) == 'OK'){
                              		$("#current-employ-first-name").val(obj.firstName) 
                              		$("#current-employ-last-name").val(obj.lastName) 
                              		$("#current-employ-email-id").val(obj.email) 
                              		$("#current-employ-user-id").val(obj.userId) 
                              		$("#current-employ-password").val(obj.password) 
                              		$("#current-employ-position").val(obj.position) 
                              		$("#current-employ-department").val(obj.deptarment)
                              } else {
                                 console.log("Logged In user data is not found!")
                                 
                              } 
											    },
                          error: function(error) {
                              console.log(error);
                          }
								});
                */




        }

});

