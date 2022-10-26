# Generated by Django 4.1.2 on 2022-10-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_item_tamanho'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='tamanho',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('NF', 'Pedido não realizado!'), ('FE', 'Pedido encaminhado!'), ('EV', 'Pedido enviado!'), ('ET', 'Entregue!'), ('DV', 'Pedido devolvido!')], max_length=2),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='usuario_pedinte',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='StatusPedido',
        ),
    ]
