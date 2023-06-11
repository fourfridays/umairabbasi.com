# Generated by Django 4.2.1 on 2023-05-31 22:52

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'link', 'code'], icon='pilcrow', template='blocks/paragraph_block.html')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')], required=False)), ('border', wagtail.blocks.BooleanBlock(help_text='Adds border around image', required=False))])), ('button_block', wagtail.blocks.StructBlock([('alignment', wagtail.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large')])), ('cta_text', wagtail.blocks.CharBlock(help_text='25 character limit.', max_length=25)), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('color', wagtail.blocks.ChoiceBlock(choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('dark-brown', 'Dark Brown'), ('white-smoke', 'White Smoke'), ('concrete', 'Concrete'), ('aqua-island', 'Aqua Island')]))])), ('image_grid_block', wagtail.blocks.StreamBlock([('grid', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='size: 800X450px', required=True)), ('caption', wagtail.blocks.CharBlock(help_text='26 characters limit', max_length=26)), ('description', wagtail.blocks.CharBlock(help_text='300 characters limit', max_length=300, required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False))]))])), ('document_block', wagtail.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert a URL         e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='code', max_width='1200', template='blocks/embed_block.html')), ('icon_block', wagtail.blocks.StructBlock([('icon', wagtail.blocks.ChoiceBlock(choices=[('font-awesome', 'Font Awesome'), ('material-icon', 'Material Icon')])), ('name', wagtail.blocks.CharBlock(help_text='25 character limit', max_length=25)), ('size', wagtail.blocks.ChoiceBlock(choices=[('sm', 'Small'), ('md', 'Medium'), ('lg', 'Large'), ('xl', 'Extra Large')])), ('font_awesome_icon_choice', wagtail.blocks.ChoiceBlock(choices=[('solid', 'Solid'), ('regular', 'Regular'), ('light', 'Light'), ('brand', 'Brand')], required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='includes/table.html')), ('code_block', wagtail.blocks.StructBlock([('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))])), ('raw_html', wagtail.blocks.StructBlock([('html', wagtail.blocks.RawHTMLBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')]))]))], blank=True, use_json_field=True, verbose_name='Page body'),
        ),
    ]
