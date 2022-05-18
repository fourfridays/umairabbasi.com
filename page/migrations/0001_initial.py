# Generated by Django 2.2.12 on 2020-06-03 23:14

from django.db import migrations, models
import django.db.models.deletion
import page.blocks
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero_heading', models.CharField(blank=True, help_text='40 character limit.', max_length=140, null=True)),
                ('hero_caption', models.CharField(blank=True, help_text='140 character limit.', max_length=140, null=True)),
                ('hero_photo_credit', models.CharField(blank=True, help_text='80 character limit. This will show on the bottom right on the image', max_length=80, null=True)),
                ('hero_cta', models.CharField(blank=True, help_text='Text to display on Call to Action. 20 character limit.', max_length=20, null=True, verbose_name='Hero CTA')),
                ('body', wagtail.fields.StreamField([('single_column', wagtail.blocks.StructBlock([('column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', page.blocks.BackgroundColorBlock())], group='COLUMNS')), ('two_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', page.blocks.BackgroundColorBlock())], group='COLUMNS')), ('three_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('middle_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', page.blocks.BackgroundColorBlock())], group='COLUMNS')), ('four_columns', wagtail.blocks.StructBlock([('left_column_1', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('left_column_2', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_1', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('right_column_2', wagtail.blocks.StreamBlock([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')]))]))])), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')])), ('background_color', page.blocks.BackgroundColorBlock())], group='COLUMNS')), ('image_grid', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))], help_text='Minimum 2 blocks and a maximum of 4 blocks', icon='image', max_num=4, min_num=2))], default='')),
                ('hero_cta_link', models.ForeignKey(blank=True, help_text='Choose a page to link the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Hero CTA link')),
                ('hero_image', models.ForeignKey(blank=True, help_text='2400X858px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254, verbose_name='First name')),
                ('last_name', models.CharField(max_length=254, verbose_name='Last name')),
                ('job_title', models.CharField(max_length=254, verbose_name='Job title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]
