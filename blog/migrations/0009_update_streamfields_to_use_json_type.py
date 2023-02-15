# Generated by Django 3.2.16 on 2022-11-16 16:38

import common.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201014_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock(icon='doc-full', label='Rich Text')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('raw_html', wagtail.blocks.RawHTMLBlock())], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image', 'code'])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('python', 'Python'), ('bash', 'Bash/Shell'), ('html', 'HTML'), ('css', 'CSS'), ('scss', 'SCSS'), ('json', 'JSON')])), ('code', wagtail.blocks.TextBlock())], label='Code Block')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')]))])), ('raw_html', wagtail.blocks.RawHTMLBlock()), ('blockquote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock()), ('source_text', wagtail.blocks.RichTextBlock(required=False)), ('source_url', wagtail.blocks.URLBlock(help_text='Source text will link to this url.', required=False))])), ('list', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='List Item'), template='common/blocks/list_block_columns.html')), ('video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock()), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')]))])), ('media_file', wagtail.blocks.StructBlock([('media', common.blocks.MediaBlock()), ('muted_autoplay_and_loop', wagtail.blocks.BooleanBlock(help_text='If checked, the media will start playing, without sound, when the page loads and loop when finished. Intended to allow videos to function as GIFs.', required=False))])), ('heading_1', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('heading_2', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('heading_3', wagtail.blocks.StructBlock([('content', wagtail.blocks.CharBlock())])), ('inline_pdf', wagtail.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))]))], use_json_field=True),
        ),
    ]