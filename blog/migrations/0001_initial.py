# Generated by Django 2.2.12 on 2020-06-03 23:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import taxonomy.models
import wagtail.contrib.routable_page.models
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('page', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date_published', models.DateField(blank=True, null=True, verbose_name='Date article published')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.fields.StreamField([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))], blank=True, verbose_name='Page body')),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('flickr_photoset_id', models.CharField(blank=True, max_length=25)),
                ('category', models.ForeignKey(blank=True, default='', limit_choices_to=taxonomy.models.Node.get_blog_categories, null=True, on_delete=django.db.models.deletion.PROTECT, to='taxonomy.Node')),
                ('hero_image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPeopleRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_person_relationship', to='blog.BlogPage')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_blog_relationship', to='page.People')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.BlogPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_blogpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('hero_image', models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]
