from aiohttp import web

@web.middleware
async def error_handler(request, handler):
    try:
        response = await handler(request)
        if response.status == 404:
            return web.json_response({'success': False, 'message': 'Запрашиваемый ресурс не найден'}, status=404)
        return response
    except web.HTTPException as ex:
        return web.json_response({'success': False, 'message': str(ex)}, status=ex.status)
    except Exception as e:
        return web.json_response({'success': False, 'message': f'Общая ошибка: {str(e)}'}, status=500)
