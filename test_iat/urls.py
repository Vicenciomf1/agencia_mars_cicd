from django.urls import path
from . import views,auth,elecciones2021

urlpatterns = [
    path('', views.index_resultados),
    path('descarga', views.descarga_resultados),
    #path('', views.index),
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout),
    #ejecucion
    path('test/<int:test_id>', views.test),
    path('test/paso1', views.paso1),
    path('test/paso2', views.paso2),
    path('test/paso3', views.paso3),
    path('test/paso4', views.paso4),
    path('test/paso5', views.paso5),
    path('test/final', views.final),
    #mantenedores
    path('cliente/', views.cliente), 
    path('cliente/new', views.cliente_new), 
    path('cliente/<int:cli_id>/edit', views.cliente_edit), 
    path('cliente/<int:cli_id>/destroy', views.cliente_destroy), 
    path('categoria/', views.categorias), 
    path('categoria/new', views.categorias_new), 
    path('categoria/<int:cat_id>/edit', views.categorias_edit), 
    path('categoria/<int:cat_id>/destroy', views.categorias_destroy), 
    path('producto/', views.producto),
    path('producto/new', views.producto_new),  
    path('producto/<int:prod_id>/edit', views.producto_edit),
    path('producto/<int:prod_id>/destroy', views.producto_destroy), 
    path('caracteristica/', views.caracteristica),
    path('caracteristica/new', views.caracteristica_new),  
    path('caracteristica/<int:car_id>/edit', views.caracteristica_edit),
    path('caracteristica/<int:car_id>/destroy', views.caracteristica_destroy), 
    path('adjetivo/', views.adjetivo),
    path('adjetivo/new', views.adjetivo_new),  
    path('adjetivo/<int:adj_id>/edit', views.adjetivo_edit),
    path('adjetivo/<int:adj_id>/destroy', views.adjetivo_destroy), 
    # creacion de test
    path('iat/', views.iat ), 
    path('iat/new', views.iat_new), 
    path('iat/<int:iat_id>/edit', views.iat_edit), 
    path('iat/<int:iat_id>/destroy', views.iat_destroy),

    
    path('iat/<int:iat_id>', views.iat_detalle ), 
    
    ### analisis categoria 
    path('iat/categoria/add/<int:iat_id>', views.iat_add_cat),
    path('iat/caracteristica/add/<int:iat_id>', views.iat_add_car),
    path('iat/caracteristica/remove/<int:iat_id>', views.iat_rem_car),
    path('iat/adjetivo/add/<int:car_id>', views.iat_add_adj),
    path('iat/adjetivo/remove/<int:adj_id>', views.iat_rem_adj),

    path('iat/resultado/<int:iat_id>/<int:user_id>', views.resultado), 
    #iat elecciones
    path('elecciones2021/start/<int:iat_id>', elecciones2021.elecciones_start),
    path('elecciones2021/test', elecciones2021.elecciones_test), 
    path('elecciones2021/end', elecciones2021.elecciones_end), 

    path('usuarios', views.usuarios), 
    path('usuarios/<int:user_id>', views.usuarios_detalle),  

    path('sondeos', views.sondeos), 

    path('sondeos/activar', views.sondeos), 
    path('sondeos/desactivar/<int:s_id>', views.sondeos_deactivate), 

]
