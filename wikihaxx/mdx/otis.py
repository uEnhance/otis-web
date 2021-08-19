import re
from typing import Any, List

import markdown
import markdown.preprocessors
from arch.models import Problem
from core.models import UnitGroup
from dashboard.models import Achievement, AchievementUnlock, PSet
from django.db.models.aggregates import Sum
from roster.models import Student


class OTISExtension(markdown.Extension):
	def extendMarkdown(self, md: Any):
		md.preprocessors.add('otis-extras', OTISPreprocessor(md), '>html_block')


special_start_regex = re.compile(r'\[(arch|diamond|unit|generic)([ a-zA-Z0-9]*)\]')
special_end_regex = re.compile(r'\[/(arch|diamond|unit|generic)+\]')


class OTISPreprocessor(markdown.preprocessors.Preprocessor):
	# TODO implement cool stuff
	def run(self, lines: List[str]) -> List[str]:
		output: List[str] = []
		active = False

		for line in lines:
			m_start = special_start_regex.match(line)
			m_end = special_end_regex.match(line)
			if m_start is not None:
				output.append(r'<div class="col-md-4 float-right">')
				table_output: List[str] = []
				table_output.append(r'<table>')
				table_output.append(r'<tbody>')
				active = True
				tag_name = m_start.group(1)
				tag_arg = m_start.group(2).strip()

				if tag_name == 'arch':
					try:
						problem = Problem.objects.get(puid__iexact=tag_arg)
					except Problem.DoesNotExist:
						table_output.append(f'<tr class="danger"><th>PUID</th><td>{tag_arg}</td></tr>')
					else:
						table_output.append(
							f'<tr><th>PUID</th><td><a href="{problem.get_absolute_url()}">' +
							r'<span class="fa fa-link"></span></a></td></tr>'
						)
						table_output.append(f'<tr><th>Source</th><td>{problem.get_source()}</td></tr>')
						if problem.aops_url:
							table_output.append(
								f'<tr><th>AoPS</th><td><a href="{problem.aops_url}">Forum link</a></td></tr>'
							)
				elif tag_name == 'diamond':
					try:
						diamond = Achievement.objects.get(code__iexact=tag_arg)
					except Achievement.DoesNotExist:
						table_output.append('<tr class="danger"><th>Code</th><td>INVALID</td></tr>')
					else:
						if diamond.image:
							output.append(
								f'<div class="W-100 text-center"><img class="w-50" src="{diamond.image.url}" /></div>'
							)
						table_output.append(f'<tr><th>Code</th><td>{tag_arg}</td></tr>')
						table_output.append(f'<tr><th>Name</th><td>{diamond.name}</td></tr>')
						table_output.append(f'<tr><th>Value</th><td>{diamond.diamonds}◆</td></tr>')
						num_found = AchievementUnlock.objects.filter(achievement=diamond).count() or 0
						table_output.append(f'<tr><th>Found by</th><td>{num_found}</td></tr>')
						table_output.append(f'<tr><th>Description</th><td>{diamond.description}</td></tr>')
				elif tag_name == 'unit':
					try:
						unitgroup = UnitGroup.objects.get(name__iexact=tag_arg)
					except UnitGroup.DoesNotExist:
						table_output.append(f'<tr class="danger"><th>Name</th><td>{tag_arg}</td></tr>')
					else:
						num_taking = Student.objects.filter(curriculum__group=unitgroup).count()
						num_psets = PSet.objects.filter(unit__group=unitgroup, approved=True).count()
						clubs_given = PSet.objects.filter(
							unit__group=unitgroup,
						).aggregate(Sum('clubs'))['clubs__sum'] or 0
						hearts_given = PSet.objects.filter(
							unit__group=unitgroup,
						).aggregate(Sum('hours'))['hours__sum'] or 0
						versions = ', '.join(u.code for u in unitgroup.unit_set.all())
						table_output.append(f'<tr><th>Name</th><td>{unitgroup.name}</td></tr>')
						table_output.append(
							f'<tr><th>Classification</th><td>{unitgroup.get_subject_display()}</td></tr>'
						)
						table_output.append(f'<tr><th>Slug</th><td>{unitgroup.slug}</td></tr>')
						table_output.append(f'<tr><th>Versions</th><td>{versions}</td></tr>')
						table_output.append(f'<tr><th>Participants</th><td>{num_taking}</td></tr>')
						table_output.append(f'<tr><th>Submissions</th><td>{num_psets}</td></tr>')
						table_output.append(f'<tr><th>♣ earned</th><td>{clubs_given}</td></tr>')
						table_output.append(f'<tr><th>♥ earned</th><td>{hearts_given}</td></tr>')

				output += table_output
			elif m_end is not None:
				output.append(r'</tbody>')
				output.append(r'</table>')
				output.append(r'</div>')
				active = False
			elif active is True:
				parts = line.split(' | ')
				if len(parts) == 2:
					output.append('<tr>')
					output.append('<th>' + parts[0].strip() + '</th>')
					output.append('<td>' + parts[1].strip() + '</td>')
					output.append('</tr>')
			else:
				output.append(line)
		return output