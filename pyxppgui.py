# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import sys
import time
import gc
import matplotlib
import wx
import wx.xrc
import os
import re

import gtk

matplotlib.use('WXAgg')
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from matplotlib.backends.backend_wxagg import Toolbar, FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

from xppcall import xpprun, read_pars, read_inits, read_numerics, read_sv

###########################################################################
## Class MainFrame
###########################################################################

matplotlib.rc('image', origin='lower')


class PlotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.parent = parent

        #self.fig = Figure()
        self.fig, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[])
        self.ax.set_autoscaley_on(True)
        self.ax.set_autoscalex_on(True)
        #self.ax.set_xlim(self.min_x, self.max_x)

        self.canvas = FigureCanvasWxAgg(self, -1, self.fig)
        self.toolbar = NavigationToolbar2Wx(self.canvas)

        self.toolbar.Realize()
        #plt.subplots_adjust(left=0.1, right=0.1, top=0.1, bottom=0.1)
        self.fig.tight_layout()
        # self.toolbar.set_active([0,1])

        # Now put all into a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL)
        # Best to allow the toolbar to resize!
        sizer.Add(self.toolbar, 0, wx.GROW)

        self.SetSizer(sizer)


        self.Fit()
        #self.Show()

    def init_plot_array(self):
        ax = self.fig.add_subplot(111)

        x = np.arange(120.0) * 2 * np.pi / 60.0
        y = np.arange(100.0) * 2 * np.pi / 50.0
        self.x, self.y = np.meshgrid(x, y)
        z = np.sin(self.x) + np.cos(self.y)
        self.im = a.imshow(z, cmap=cm.jet)  # , interpolation='nearest')

        zmax = np.amax(z) - ERR_TOL
        ymax_i, xmax_i = np.nonzero(z >= zmax)
        if self.im.origin == 'upper':
            ymax_i = z.shape[0] - ymax_i
        self.lines = a.plot(xmax_i, ymax_i, 'ko')

        self.toolbar.update()  # Not sure why this is needed - ADS

    def init_plot(self,x,y,title='',xlabel='',ylabel=''):

        #self.ax.clear()

        self.lines.set_xdata(x)#plot(x,y)
        self.lines.set_ydata(y)
    
        self.ax.relim()
        self.ax.autoscale_view()


        self.canvas.draw()        
        self.canvas.flush_events()

        self.toolbar.update()  # Not sure why this is needed - ADS
        #plt.subplots_adjust(left=0.1, right=0.1, top=0.1, bottom=0.1)
        self.fig.tight_layout()
    
    def GetToolBar(self):
        # You will need to override GetToolBar if you are using an
        # unmanaged toolbar in your frame
        return self.toolbar

    def onEraseBackground(self, evt):
        # this is supposed to prevent redraw flicker on some X servers...
        pass





class MainFrame ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,650 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
    
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Equations = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
        
        Equations = wx.BoxSizer( wx.VERTICAL )
        
        self.eqn_txt = wx.StaticText( self.Equations, wx.ID_ANY, u"Equations", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.eqn_txt.Wrap( -1 )

        Equations.Add( self.eqn_txt, 0, wx.ALL, 5 )
        
        self.eqnDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_MULTILINE )
        self.eqnDisplay.CanCut()
        self.eqnDisplay.CanPaste()
        self.eqnDisplay.CanCopy()
        self.eqnDisplay.CanUndo()
        Equations.Add( self.eqnDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer1.Add( Equations, 2, wx.EXPAND, 5 )
        
        Parameters = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText11 = wx.StaticText( self.Equations, wx.ID_ANY, u"Parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        Parameters.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.paramDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        Parameters.Add( self.paramDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        gSizer1.Add( Parameters, 2, wx.EXPAND, 5 )
        
        Initial_Conditions = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText111 = wx.StaticText( self.Equations, wx.ID_ANY, u"Initial Conditions", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )
        Initial_Conditions.Add( self.m_staticText111, 0, wx.ALL, 5 )
        
        self.initDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        Initial_Conditions.Add( self.initDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        gSizer1.Add( Initial_Conditions, 2, wx.EXPAND, 5 )        
        Options = wx.BoxSizer( wx.VERTICAL )
        

        self.m_staticText1111 = wx.StaticText( self.Equations, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1111.Wrap( -1 )
        Options.Add( self.m_staticText1111, 0, wx.ALL, 5 )
        
        self.optDisplay = wx.TextCtrl( self.Equations, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        Options.Add( self.optDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        gSizer1.Add( Options, 2, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        self.filenameDisplay = wx.StaticText( self.Equations, wx.ID_ANY, u"No ODE file loaded.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.filenameDisplay.Wrap( -1 )
        bSizer9.Add( self.filenameDisplay, 0, wx.ALL, 5 )
        
        
        gSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.VERTICAL )


        self.openButton = wx.Button( self.Equations, wx.ID_ANY, u"Open...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.openButton, 0, wx.ALL, 5 )

        self.saveButton = wx.Button( self.Equations, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.saveButton, 0, wx.ALL, 5 )


        
        gSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        
        self.Equations.SetSizer( gSizer1 )
        self.Equations.Layout()
        gSizer1.Fit( self.Equations )
        self.m_notebook1.AddPage( self.Equations, u"Equations", True )



        self.Output = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        ## xpp output
        # text box for xpp output
        self.outDisplay = wx.TextCtrl( self.Output, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
        bSizer3.Add( self.outDisplay, 1, wx.ALL|wx.EXPAND, 5 )
        
        # set sizer for output
        self.Output.SetSizer( bSizer3 )
        self.Output.Layout()
        bSizer3.Fit( self.Output )
        self.m_notebook1.AddPage( self.Output, u"Output", False )


        
        ## graphs
        
        # graph panel
        self.Graphs = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        
        # set sizer for graph panel
        sizergraphs = wx.BoxSizer( wx.VERTICAL )		


        # set sizer for buttons
        sizerbuttons = wx.BoxSizer( wx.HORIZONTAL )

        # x coordinate text
        self.plt_optx = wx.StaticText( self.Graphs, wx.ID_ANY, u"Plot x:", wx.DefaultPosition, wx.DefaultSize)
        sizerbuttons.Add(self.plt_optx)

        # drop-down list 1 above plot window 
        self.sv_choicex = wx.Choice( choices=['-'],parent=self.Graphs, id=wx.ID_ANY,pos=wx.DefaultPosition)
        sizerbuttons.Add(self.sv_choicex)

        # y coordinate text
        self.plt_opty = wx.StaticText( self.Graphs, wx.ID_ANY, u"\tPlot y:", wx.DefaultPosition, wx.DefaultSize)
        sizerbuttons.Add(self.plt_opty)
            
        # second dropdown list
        self.sv_choicey = wx.Choice( choices=['-'], parent=self.Graphs, id=wx.ID_ANY,pos=wx.DefaultPosition)
        sizerbuttons.Add(self.sv_choicey)
        
        # add note on control
        self.hint_specific = wx.StaticText( self.Graphs, wx.ID_ANY, u"\tTo zoom in/out, selct the move button below, then hold Ctrl+Right click and move the mouse around.", wx.DefaultPosition, wx.DefaultSize)
        sizerbuttons.Add(self.hint_specific)



        sizergraphs.Add(sizerbuttons)



        # plot window
        self.graphpanel = wx.Panel(self.Graphs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizergraphs.Add(self.graphpanel,1, wx.EXPAND |wx.ALL, 5)
        #sizergraphs.Fit(self.graphpanel)
        
        self.Graphs.SetSizer(sizergraphs)
        self.Graphs.Layout()
        self.Graphs.Fit()

        # default plot values
        self.plotx = [0]
        self.ploty = [0]

        # add graphs panel to tabs
        self.m_notebook1.AddPage( self.Graphs, u"Graphs", False )




        # main sizer        
        bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
        self.SetSizer( bSizer1 )
        self.Layout()
        
        
        filemenu = wx.Menu()
        recent = wx.Menu()
        windowmenu = wx.Menu()

        
        # filemenu
        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN,"Open...","Open an ODE file")
        menuRecent = filemenu.AppendMenu(wx.ID_ANY,"&Recent Files", recent)
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        
        # windowmenu
        menuWindow = windowmenu.Append(wx.ID_ANY,"Fit","Fit Data Plot")
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(windowmenu,"&Window") # Adding the "filemenu" to the MenuBar

        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        # menu events
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU_RANGE, self.on_file_history, id=wx.ID_FILE1, id2=wx.ID_FILE9)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.WindowFit, menuWindow)

        # button events
        self.Bind(wx.EVT_BUTTON, self.RunAndSave, self.saveButton)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.openButton)
        

        # plot resize event
        self.Bind(wx.EVT_SIZE, self.OnSize) 


        # plot menu event
        self.Bind(wx.EVT_CHOICE, self.onSVSelectx, self.sv_choicex)
        self.Bind(wx.EVT_CHOICE, self.onSVSelecty, self.sv_choicey)


        # matplotlib panel
        self.plotpanel = PlotPanel(self.graphpanel)


        # some default values
        self.fullname = ''

        self.Show(True)

    def UpdateParams(self,e,plist):
        """
        update parameter list 
        """
        
        for p in plist:
            pass
        pass

        
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def h2xppcall(self,a):
        """
        convert human-readable format into xppcall compatible format
        e.g. convert 'q=2,r=1.1' to {'q':2,'r':1.1}
        OR
        convert 'q=2\n r=1.1' to {'q':2,'r':1.1}
        """
        # convert all newline to commas
        a = a.replace("\n",",")
        
        # remove spaces
        a = a.replace(" ","")
        
        # split on commas
        a = a.split(",")

        pardict = {}
        #print 'abefore', parlist

        # for each parameter, add to dictionary
        for i in range(len(a)):
            par = a[i].split('=')
            pardict[par[0]]=float(par[1])

        #print 'a',pardict
        return pardict
            

    def xppcall2h(self,a):
        """
        convert xppcall format to human-readable format.
        e.g. convert {'g':10,'n':2} to 'g=10\n n=2'
        """
        alist = ''
        for i in a:
            alist += str(i)+'='+a[i]+'\n'

        # remove trailing \n
        alist = alist.rstrip()
        
        return alist

    def WindowFit(self,e):
        """
        fit plot data
        """
        xmin = np.amin(self.plotx)
        xmax = np.amax(self.plotx)
        self.plotpanel.ax.set_xlim(xmin,xmax)

        ymin = np.amin(self.ploty)
        ymax = np.amax(self.ploty)
        self.plotpanel.ax.set_ylim(ymin,ymax)

        self.plotpanel.canvas.draw()

    def OnOpen(self,e):
        """ Open a file"""
        self.firstrun = True
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "ODE files (*.ode)|*.ode|All Files (*.*)|*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            #print self.filename,self.dirname
            self.fullname = os.path.join(self.dirname, self.filename)
            f = open(self.fullname, 'r')


            ## extract relevant information

            # read equations and display
            self.eqnDisplay.SetValue(f.read())

            # read parameters and display
            self.params = read_pars(self.fullname)            
            self.paramDisplay.SetValue(self.xppcall2h(self.params))

            # read initial conditions and display
            self.inits = read_inits(self.fullname)
            self.initDisplay.SetValue(self.xppcall2h(self.inits))
            
            # read options and display
            self.opts = read_numerics(self.fullname)
            self.optDisplay.SetValue(self.xppcall2h(self.opts))


            # update filename
            self.filenameDisplay.SetLabel('Loaded '+self.filename)




            f.close()
        dlg.Destroy()
        
    def on_file_history(self, event):
        fileNum = event.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
        self.filehistory.AddFileToHistory(path)  # move up the list
        # do whatever you want with the file path...


    def OnSize(self, event): 
        size = self.Graphs.GetClientSize() 
        #self.plotpanel.canvas.SetClientSize((size[0],size[1]*.8))
        self.plotpanel.SetClientSize((size[0],size[1]*.9))
        event.Skip()

    def onSVSelectx(self, event):
        #print "You selected: " + self.sv_choicex.GetStringSelection()
        #obj = self.sv_choicex.GetClientData(self.sv_choicex.GetSelection())
        self.choicex = self.sv_choicex.GetStringSelection()
        if self.choicex == 't':
            self.plotx = self.t
        else:
            self.plotx = self.sv[:,self.vn.index(self.choicex)]
            
        self.plotpanel.init_plot(self.plotx,self.ploty)

    def onSVSelecty(self, event):
        #print "You selected: " + self.sv_choicex.GetStringSelection()
        #obj = self.sv_choicex.GetClientData(self.sv_choicex.GetSelection())
        self.choicey = self.sv_choicey.GetStringSelection()
        if self.choicey == 't':
            self.ploty = self.t
        else:
            self.ploty = self.sv[:,self.vn.index(self.choicey)]
            
        self.plotpanel.init_plot(self.plotx,self.ploty)


    def RunAndSave(self,e):
        if (self.paramDisplay.GetValue() == '') and\
           (self.optDisplay.GetValue() == '') and\
           (self.initDisplay.GetValue() == ''):
            dlg = wx.MessageDialog( self, "Please load an ODE file first.", "Error", wx.OK)
            dlg.ShowModal() # Show it
            dlg.Destroy() # finally destroy it when finished.
            return
        try:
            # get parameter values from windows
            self.params = self.h2xppcall(self.paramDisplay.GetValue())
            self.opts = self.h2xppcall(self.optDisplay.GetValue())
            self.inits = self.h2xppcall(self.initDisplay.GetValue())
            
            # http://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one-in-python
            # parameters and options are input in the same dictionary.
            combinedin = dict(self.params.items() + self.opts.items())

            print 'running xpp with options',combinedin, self.inits
            self.npa, self.vn, fullfilename,outputfilepath = xpprun(self.fullname, 
                                                                     parameters=combinedin,
                                                                     inits=self.inits,
                                                                     clean_after=False,return_tempname=True)
            
            #print self.npa, self.vn
            self.t = self.npa[:,0]
            self.sv = self.npa[:,1:]

            if self.firstrun:
                # show simple plot by default
                # set default plot choice
                self.choicex = 't'
                self.choicey = self.vn[0]

                self.plotx = self.t
                self.ploty = self.npa[:,1]
                self.firstrun = False
            else:
                if self.choicex == 't':
                    self.plotx = self.t
                else:
                    self.plotx = self.sv[:,self.vn.index(self.choicex)]
                self.ploty = self.sv[:,self.vn.index(self.choicey)]

            # update graph tab
            self.plotpanel.init_plot(self.plotx,self.ploty)

            # update data tab
            f = open(outputfilepath, 'r')
            self.outDisplay.SetValue(f.read())
            f.close()

            # clean temporary ode files
            os.remove(outputfilepath)
            os.remove(fullfilename)
            #os.remove(fullfilename)

            # set x vs y plot options 
            # loop over dictionary to extract state variables
            svlist = ['t']
            for i in self.vn:
                svlist.append(i)

            # update the drop-down menus
            self.sv_choicex.SetItems(svlist)
            self.sv_choicey.SetItems(svlist)

        except IOError:
            # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
            dlg = wx.MessageDialog( self, "Please load an ODE file first.", "Error", wx.OK)
            dlg.ShowModal() # Show it
            dlg.Destroy() # finally destroy it when finished.



    def __del__( self ):
        pass
	

ex = wx.App() 
MainFrame(None) 
ex.MainLoop()
