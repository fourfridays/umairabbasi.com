module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            dist: {
                src: ['src/jquery-2.2.4.js', 'node_modules/bootstrap-sass/assets/javascripts/bootstrap/transition.js', 'node_modules/bootstrap-sass/assets/javascripts/bootstrap/collapse.js', 'src/umairabbasi.js'],
                dest: 'dist/js/umairabbasi.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                compress: {},
                beautify: true
        },
        dist: {
            files: {
                '../static/js/umairabbasi.min.js': ['<%= concat.dist.dest %>'],
            }
        }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          '../static/css/umairabbasi.css': 'src/umairabbasi.scss'
          //'//Volumes/autopub/iamahornet.com/global/css/main.css': 'src/main.scss',
          //'//Volumes/autopub/www.emporia.edu/global/css/main.css': 'src/main.scss'      // 'destination': 'source'
        }
      }
    },
    watch: {
      scripts: {
        files: 'src/*.*',
        tasks: ['concat', 'uglify', 'sass'],
        options: {
          livereload: true
        },
      },
    }
    });

    // Load the plugin that provides the "uglify" task.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).

    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'watch']);

};