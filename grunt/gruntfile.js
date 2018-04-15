module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        concat: {
            dist: {
                src: ['node_modules/jquery/dist/jquery.slim.min.js', 'node_modules/bootstrap/js/dist/util.js', 'node_modules/bootstrap/js/dist/collapse.js', 'src/fa-brands.min.js', 'src/fa-solid.min.js', 'src/fontawesome.min.js', 'src/umairabbasi.js'],
                dest: 'dist/js/umairabbasi.js'
            }
        },
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n',
                mangle: true,
                compress: true,
                beautify: false
        },
        dist: {
            files: {
              '/home/fourfridays/sites/umairabbasi/static/js/umairabbasi.min.js': ['<%= concat.dist.dest %>'],
              //'../static/js/umairabbasi.min.js': ['<%= concat.dist.dest %>'],
            }
        }
    },
    sass: {                              // Task
      dist: {                            // Target
        files: {                         // Dictionary of files
          '/home/fourfridays/sites/umairabbasi/static/css/umairabbasi.css': 'src/umairabbasi.scss'
          //'../static/css/umairabbasi.css': 'src/umairabbasi.scss'
        }
      }
    },
    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: '../static/css',
          src: ['*.css', '!*.min.css'],
          dest: '../static/css',
          ext: '.min.css'
        }]
      }
    },
    watch: {
      scripts: {
        files: 'src/*.*',
        tasks: ['concat', 'uglify', 'sass', 'cssmin'],
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
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).

    grunt.registerTask('default', ['concat', 'uglify', 'sass', 'cssmin', 'watch']);

};
