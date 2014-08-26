(function() {
    var app = angular.module("ebsApp", []);

    app.controller("ProjectController", ['$scope', function($scope) {
        $scope.project = {
            image: '',
            imageName: '',
            imageUrl: '_ah/img/encoded_gs_file:ZWJzLWVuZ2luZWVyaW5nLXVwbG9hZHMvaW1hZ2VzL3Byb2plY3QvMjAxNC8wNy8yNi8wNi0yMDE1LXBvcnNjaGUtY2F5bWFuLWd0cy1xcy0xXzEuanBn=s384',
            title: 'Porsche Cayman GTS',
            description: '',
            url: '',
        };
    }]);

    app.directive("projectSlider", function() {
        return {
            restrict: "E",
            templateUrl: DJANGO_STATIC_URL+"main/client-templates/project-slider.html"
        };
    });

})();


//  {% for project in latest_projects %}
//  <li>
//    <div class="row">
//      <div class="col-md-4">
//        <div class="image-container">
//          {% with project.images.all|first as image %}
//            <img src="{{ image.image.url }}=s384" alt="{{ image.name }}" class="project-image">
//            <!--a href="{{ object.docfile.url }}">{{ object.docfile.name }}</a-->
//          {% endwith %} 
//        </div><!--/.image-container -->
//      </div><!--/.col-md-4 -->
//      <div class="col-md-8">
//        <h3>{{ project.title }}</h3>
//        <p>{{ project.description|truncatewords:49 }} <a href="{% url 'project:project_detail' project.id %}" class="expand"><span>Show More <span class="icon-resize-full"></span></span></p></a>
//      </div><!--/.col-md-8 -->
//    </div><!--/.row -->
//  </li>            
//  {% endfor %}