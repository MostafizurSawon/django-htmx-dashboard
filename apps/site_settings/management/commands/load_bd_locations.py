import json

from django.core.management.base import BaseCommand

from apps.site_settings.models import BD_District, BD_Division, BD_Upazila


class Command(BaseCommand):
    help = 'Load BD Divisions, Districts, Upazilas from separate JSON files'

    def handle(self, *args, **options):
        data_dir = 'apps/site_settings/data/'

        # Step 1: Divisions লোড (ফাইল নাম bd-divisions.json)
        try:
            with open(data_dir + 'bd-divisions.json', 'r', encoding='utf-8') as f:
                divisions_data = json.load(f)
                divisions_list = divisions_data.get('divisions', divisions_data)  # যদি root list হয় বা key 'divisions' হয়
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Divisions file error: {e}"))
            return

        created_div = 0
        for item in divisions_list:
            if not isinstance(item, dict):
                continue
            div, created = BD_Division.objects.get_or_create(
                id=item.get('id'),  # ID store করো যদি থাকে
                defaults={
                    'name': item.get('name') or item.get('division', ''),
                    'name_bn': item.get('bn_name', ''),
                }
            )
            if created:
                created_div += 1

        self.stdout.write(self.style.SUCCESS(f'Loaded {created_div} Divisions'))

        # Step 2: Districts লোড
        try:
            with open(data_dir + 'bd-districts.json', 'r', encoding='utf-8') as f:
                districts_data = json.load(f)
                districts_list = districts_data.get('districts', districts_data)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Districts file error: {e}"))
            return

        created_dist = 0
        for item in districts_list:
            if not isinstance(item, dict):
                continue
            try:
                div = BD_Division.objects.get(id=item['division_id'])  # division_id দিয়ে link
                dist, created = BD_District.objects.get_or_create(
                    division=div,
                    id=item.get('id'),
                    defaults={
                        'name': item.get('name') or item.get('district', ''),
                        'name_bn': item.get('bn_name', ''),
                    }
                )
                if created:
                    created_dist += 1
            except BD_Division.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Division ID {item.get('division_id')} not found for district {item.get('name')}"))
                continue

        self.stdout.write(self.style.SUCCESS(f'Loaded {created_dist} Districts'))

        # Step 3: Upazilas লোড
        try:
            with open(data_dir + 'bd-upazilas.json', 'r', encoding='utf-8') as f:
                upazilas_data = json.load(f)
                upazilas_list = upazilas_data.get('upazilas', upazilas_data)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Upazilas file error: {e}"))
            return

        created_upa = 0
        for item in upazilas_list:
            if not isinstance(item, dict):
                continue
            try:
                dist = BD_District.objects.get(id=item['district_id'])  # district_id দিয়ে link
                upa, created = BD_Upazila.objects.get_or_create(
                    district=dist,
                    id=item.get('id'),
                    defaults={
                        'name': item.get('name') or item.get('upazila', ''),
                        'name_bn': item.get('bn_name', ''),
                    }
                )
                if created:
                    created_upa += 1
            except BD_District.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"District ID {item.get('district_id')} not found for upazila {item.get('name')}"))
                continue

        self.stdout.write(self.style.SUCCESS(f'Loaded {created_upa} Upazilas'))
        self.stdout.write(self.style.SUCCESS('✅ All locations loaded!'))