import gossip
from eva import conf

@gossip.register('eva.interaction', provides=['echo'])
def interaction(context):
    prefix = conf['plugins']['echo']['config']['echo_prefix']
    context.set_output_text('%s%s' %(prefix, context.get_input_text()))
    context.conversation.close()
