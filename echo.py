import gossip
from eva import conf

@gossip.register('eva.interaction', priority=-100, provides=['echo'])
def interaction(context):
    if not context.response_ready():
        prefix = conf['plugins']['echo']['config']['echo_prefix']
        context.set_output_text('%s%s' %(prefix, context.get_input_text()))
        # Close conversation if plugin is used.
        try: context.conversation.close()
        except: pass
