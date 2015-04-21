import ansible.playbook
import ansible.constants as C
import ansible.utils.template
from IPython import embed
from ansible.callbacks import DefaultRunnerCallbacks, AggregateStats

class PlaybookCallbacks(object):
	def __init__(self, verbose=False):
		self.verbose = verbose

	def on_start(self):
		pass

	def on_notify(self, host, handler):
		pass

	def on_no_hosts_matched(self):
		pass

	def on_no_hosts_remaining(self):
		pass

	def on_task_start(self, name, is_conditional):
		print name
		pass

	def on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
		pass

	def on_setup(self):
		pass

	def on_import_for_host(self, host, imported_file):
		pass

	def on_not_import_for_host(self, host, missing_file):
		pass

	def on_play_start(self, name):
		pass

	def on_stats(self, stats):
		pass


class PlaybookRunnerCallbacks(DefaultRunnerCallbacks):
	pass



class Sensible(object):
	def __init__(self, inventory_file, playbook_file, vault_pass=None):
		self.vault_pass = vault_pass

		self.pb = ansible.playbook.PlayBook(
				playbook=playbook_file,
				inventory = ansible.inventory.Inventory(inventory_file, vault_password=self.vault_pass),
				callbacks = PlaybookCallbacks(),
				runner_callbacks = PlaybookRunnerCallbacks(),
				stats = AggregateStats())
		self.run = self.pb.run

	@property
	def plays(self):
		return [ansible.playbook.Play(self.pb, play_ds, play_basedir, vault_password=self.pb.vault_password)
				for (play_ds, play_basedir) in zip(self.pb.playbook, self.pb.play_basedirs)]

	@property
	def tasks(self):
		# get list of tasks
		t = []
		for play in self.plays:
			t.append(self.pb.tasks_to_run_in_play(play))
		return t
	
	@property
	def hosts(self):
		h = []
		for play in self.plays:
			h += self.pb.inventory.list_hosts(play.hosts)
		return h

s = Sensible('inventory', 'playbook.yml')
embed()
