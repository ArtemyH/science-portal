import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        subprocess.run(['ls'])
        # subprocess.run(['cd scrapper && scrapy crawl elibrary'])
        # subprocess.run(['cd scrapper/', 'scrapy crawl elibrary'])
