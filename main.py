from nicegui import ui
ui.add_head_html('''
    <style type="text/tailwindcss">
        @layer components {
            .green-box {
                @apply bg-green-400;
            }
        }
    </style>
''')
ui.label('Theodore Roosevelt').classes('text-4xl')
ui.label('''Former President of the United States with a
        robust legacy in progressive reforms,
        conservation, and foreign policy. Post-presidency,
        continued to be an influential figure
        in American politics and global affairs through writing,
        exploration, and advocating for
        social and political reforms.''')
ui.separator()

with ui.splitter(reverse=True, value=30).classes('w-screen border-none w-0') as splitter:
    with splitter.before:
        ui.label('Professional Experience').classes('green-box')
        with ui.row().classes('h-0'):
            ui.icon('commit', color='green')
            ui.label('26th President of the United States of America').classes('font-bold')
        ui.label('Washington, D.C. ● Sep 1901 - Mar 1909').classes('indent-8 h-2')
        ui.markdown('''
            - Implemented progressive policies and reforms known as the "Square Deal."
            - Established numerous national parks, forests, and monuments, laying the foundation for the modern conservation movement.
            - Negotiated the end of the Russo-Japanese War, for which he won the Nobel Peace Prize.
            - Strengthened the U.S. Navy and supported the construction of the Panama Canal.
            ''')
        with ui.row().classes('h-0'):
            ui.icon('commit', color='green')
            ui.label('Governor of New York').classes('font-bold')
        ui.label('Albany, NY ● January 1899 - December 1900').classes('indent-8 h-2')
        ui.markdown('''
        - Implemented progressive policies including civil service reform and labor rights.
        ''')
        with ui.row().classes('h-0'):
            ui.icon('commit', color='green')
            ui.label('Assistant Secretary of the Navy').classes('font-bold')
        ui.label('Washington, D.C. ● April 1897 - May 1898').classes('indent-8 h-2')
        ui.markdown('''
        - Strengthened the Navy and prepared it for future conflicts, including the Spanish-American War.
        ''')
        with ui.row().classes('h-0'):
            ui.icon('commit', color='green')
            ui.label('New York City Police Commissioner').classes('font-bold')
        ui.label('New York, NY ● May 1895 - April 1897').classes('indent-8 h-2')
        ui.markdown('''
            - Reformed the police department, focusing on eliminating corruption and improving efficiency.
        ''')
        ui.label('Education').classes('green-box')
        with ui.row().classes('h-0'):
            ui.icon('commit', color='green')
            ui.label('Harvard University').classes('font-bold')
        ui.label('Cambridge, MA ● July 1876 - December 1880').classes('indent-8 h-2')
        ui.markdown('''
            -  Bachelor of Arts in History and Government
        ''')

    with splitter.after:
        ui.label('Profile').classes('text-right green-box')
        with ui.row().classes('border-0'):
            ui.icon('place')
            ui.label('Oyster Bay, NY')
        with ui.row():
            ui.icon('call')
            ui.label('(518) 474-8390')
        with ui.row():
            ui.icon('mail')
            ui.label('theodore.roosevelt@sagamorehill.org')
        ui.label('Skills').classes('text-right green-box border-0')
        ui.label('Leadership and Public Speaking').classes('h-0')
        ui.label('Policy Analysis and Political Strategy').classes('h-0')
        ui.label('Conservation and Environmental Advocacy').classes('h-0')
        ui.label('Writing and Journalism').classes('h-0')
        ui.label('Exploration and Expedition Planning').classes('h-0')
        ui.label('Honors and Awards').classes('text-right green-box border-0')
        ui.label('Nobel Peace Prize (1906)').classes('h-0')
        ui.label('Medal of Honor').classes('h-0')

ui.run()
