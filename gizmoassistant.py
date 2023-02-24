# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy


bl_info = {
    'name': 'GizmoAssistant',
    'author': 'Tanner Morgan',
    'description': 'A helpful addon for your Gizmo needs',
    'blender': (3, 0, 0),
    'version': (0, 0, 1),
    'location': 'View3D',
    'wiki_url': 'https://github.com/tmorgan497/GizmoAssistant/wiki',
    'category': '3D View',
}


class GizmoAssistant(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_gizmo_assistant"
    bl_label = "Gizmo Assistant"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        self.layout.label(text="Gizmo Assistant")


class GizmoAssistantPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__
    # add checkupdate operator button
    check_update: bpy.props.BoolProperty(
        name="Check for Update",
        description="If enabled, addon will check for updates",
        default=True,
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Gizmo Assistant Preferences")
        layout.prop(self, "check_update")


def register():
    bpy.utils.register_class(GizmoAssistant)
    bpy.utils.register_class(GizmoAssistantPreferences)


def unregister():
    bpy.utils.unregister_class(GizmoAssistant)
    bpy.utils.unregister_class(GizmoAssistantPreferences)


if __name__ == "__main__":
    bpy.utils.register_class(GizmoAssistant)
