from django.shortcuts import render, redirect
from .forms import SDGMetadataForm, SearchForm
from .models import SDGMetadata
from django.db.models import Q
import yaml
from django.http import HttpResponse
from django.shortcuts import render


import logging

logger = logging.getLogger(__name__)

def submit_metadata(request):
    logger.info("Rendering metadata form")
    if request.method == "POST":
        logger.info("Received POST request")
        form = SDGMetadataForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Form saved successfully")
            return redirect('success')
        else:
            logger.warning("Form is invalid")
    else:
        form = SDGMetadataForm()

    return render(request, 'metadata_form.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def submit_metadata(request):
    if request.method == "POST":
        form = SDGMetadataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SDGMetadataForm()
    return render(request, 'metadata_form.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def search_projects(request):
    form = SearchForm(request.GET)
    projects = SDGMetadata.objects.none()  # Start with an empty queryset.

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            keywords = query.split()  # Split query into multiple words
            
            q_objects = Q()
            for keyword in keywords:
                q_objects |= Q(project_name__icontains=keyword)
                q_objects |= Q(description__icontains=keyword)
                q_objects |= Q(sdg_targets__icontains=keyword)  # Search in SDG metadata

            projects = SDGMetadata.objects.filter(q_objects)

    # If download is requested, handle the YAML file creation and send it as a download
    if request.GET.get('download') == 'true' and projects.exists():
        project = projects.first()  # Get the first matching project
        
        project_data = {
            'project_name': project.project_name,
            'description': project.description,
            'github_url': project.github_url,
            'sdg_targets': project.sdg_targets,
        }
        
        yaml_content = yaml.dump(project_data, default_flow_style=False)

        response = HttpResponse(yaml_content, content_type="application/x-yaml")
        response['Content-Disposition'] = f'attachment; filename="{project.project_name}.yaml"'

        return response

    return render(request, 'search_results.html', {'form': form, 'projects': projects})